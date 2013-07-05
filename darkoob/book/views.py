from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.db import transaction

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
    from darkoob.migration.models import Migration

    m = Migration() 

    return render(request, template ,{
        # 'is_favorite_book': is_favorite_book,
        'new_review_form': NewReviewForm(),
        'book': book,
        'rate': book.rating.get_rating(),
        'reviews': reviews,
        'count': count[::-1],
        'migrations': Migration.objects.filter(book=book),
    })


from avatar.templatetags import avatar_tags


def book_lookup(request):
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            model_results = Book.objects.filter(title__icontains=value)
            results = [ {'book_title': x.title ,'book_id':x.id ,'photo': x.thumb.url , 'author_name': x.author_names() }  for x in model_results]

    to_json = []

    jt=simplejson.dumps(results)
    print jt
    return HttpResponse(jt, mimetype='application/json')
    
