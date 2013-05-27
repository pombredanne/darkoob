from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from darkoob.book.models import Book

def page(request, book_id, book_title):
    return render(request, "book/book_page.html")
