from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from darkoob.book.models import Book
from django.utils import simplejson


from darkoob.book.models import Review

def page(request, book_id, book_title):
    book = Book.objects.get(id = book_id, title = book_title)
    template = 'book/book_page.html'
    reviews = Review.objects.filter(book=book).order_by("-submitted_time")
    count = range(1, len(reviews) + 1)

    if request.is_ajax():
        template = 'book/reviews.html'

    if book:
        return render(request, template ,{
            'book': book,
            'rate': book.rating.get_rating(),
            'reviews': reviews,
            'count': count[::-1],
        })
    else:
        raise Http404

def book_lookup(request):
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            #if len(val) > 2:
            model_results = Book.objects.filter(title__icontains=value)
            results = [ x.title  for x in model_results]
    to_json = {'options':results}
    jt=simplejson.dumps(to_json)
    return HttpResponse(jt, mimetype='application/json')

# @login_required
# def rate(request, rate):
#     if request.method == 'POST':
#         return HttpResponse("sabt shod")
#     else:
#         return HttpResponse("error")
        
