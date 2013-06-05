from django.conf.urls import patterns, include, url
from darkoob.book import views as book_views

urlpatterns = patterns('',
    url(r'^(?P<book_id>\d+)/(?P<book_title>\w+)/$', book_views.page, name='book_page'),
    # url(r'^rate/$', book_views.rate, name='rate'),
)
