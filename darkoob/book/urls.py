from django.conf.urls import patterns, include, url
from darkoob.book import views as book_views

urlpatterns = patterns('',
    url(r'^(?P<book_id>\d+)/(?P<book_title>[a-zA-Z0-9\-_]+)/$', book_views.page, name='book_page'),
    url(r'^look/$', book_views.book_lookup),
    url(r'^author/$', book_views.author_lookup),
    # url(r'^rate/$', book_views.rate, name='rate'),
)
