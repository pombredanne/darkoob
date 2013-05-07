from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from darkoob import views 
from darkoob import ajax 

from search.views import *

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
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


    # Search 
    # TODO: Move to search application
    url(r'^user/$',user_search_page),
    url(r'^users/$',ajax_result_of_user_search),
)
