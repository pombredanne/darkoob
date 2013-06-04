from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from darkoob import views 
from darkoob import ajax 


dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # search url
    url(r'^search/', include('haystack.urls')),
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # Static URL
    url(r'', include('django.contrib.staticfiles.urls')),

    # Dajaxice URLs 
    url(r'^ajaxice', views.index),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Project-specific URLs
    url(r'^$', views.index, name='index'),
    url(r'', include('darkoob.social.urls', namespace='social', app_name='socials')),
    url(r'', include('darkoob.migration.urls', namespace='migration')),

    url(r'^book/', include('darkoob.book.urls', namespace='book')),
    url(r'^group/', include('darkoob.group.urls', namespace='group')),
    # Search 
    # TODO: Move to search application
    url(r'', include('darkoob.search.urls', namespace='search')),

    # url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^avatar/', include('avatar.urls')),



)
