from django.conf.urls import patterns, include, url
from darkoob.search import views as search_views



urlpatterns = patterns('',
    url(r'^user/$', search_views.search_user),
    url(r'^users/$', search_views.search_user_result),
    url(r'^uu/$', search_views.entry_index),
    url(r'^uu1/$', search_views.entry_index1),
    url(r'^search/look/$', search_views.search_lookup),
)