from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from darkoob import views 
from darkoob import ajax 

from django.contrib.auth.views import login, logout
######################
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
######################
admin.autodiscover()

urlpatterns = patterns('',
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),
    # Static URL
    url(r'', include('django.contrib.staticfiles.urls')),

    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # Auth URL's
    # (r'^accounts/login/$',  login, {'template_name': 'login.html'}),
    # (r'^accounts/logout/$', logout),

    url(r'^$', views.index, name='index'),
    url(r'', include('darkoob.social.urls', namespace='social', app_name='socials')),

    # Dajaxice URLs 
    url(r'^ajaxice',views.BasicPage),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
