from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


from darkoob import views 


######################
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
######################
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darkoob.views.home', name='home'),
    # url(r'^darkoob/', include('darkoob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #static url
    url(r'', include('django.contrib.staticfiles.urls')),


    url(r'^home/',views.BasicPage),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^main/', include('darkoob.main.urls')),

)
