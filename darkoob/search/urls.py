from django.conf.urls import patterns, include, url
from darkoob.search import views as search_views



urlpatterns = patterns('',
    url(r'^user/$', search_views.search_user),
    url(r'^users/$', search_views.search_user_result),
)