from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from darkoob.book.models import Book
from darkoob.book.forms import NewReviewForm
from django.utils import simplejson


from darkoob.book.models import Review

def page(request, book_id, book_title):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    template = 'book/book_page.html'
    reviews = Review.objects.filter(book=book).order_by("-rating_score")
    count = range(1, len(reviews) + 1)

    if request.is_ajax():
        template = 'book/reviews.html'


    return render(request, template ,{
        'new_review_form': NewReviewForm(),
        'book': book,
        'rate': book.rating.get_rating(),
        'reviews': reviews,
        'count': count[::-1],
    })


from avatar.templatetags import avatar_tags


def book_lookup(request):
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            model_results = Book.objects.filter(title__icontains=value)
            results = [ {'book_title': x.title , 'photo': x.thumb.url , 'author_name': x.author_names() }  for x in model_results]

    to_json = []

    jt=simplejson.dumps(results)
    return HttpResponse(jt, mimetype='application/json')
