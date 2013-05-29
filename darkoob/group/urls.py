from django.conf.urls import patterns, include, url
from darkoob.group import views as group_view

urlpatterns = patterns('',
    url(r'^(?P<group_id>\d+)/(?P<group_name>\w+)/$', group_view.group, name='group_page'),
    # url(r'^rate/$', book_views.rate, name='rate'),
)
