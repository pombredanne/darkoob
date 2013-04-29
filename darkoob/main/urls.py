from django.conf.urls import patterns, include, url

from darkoob.main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darkoob.views.home', name='home'),
    # url(r'^darkoob/', include('darkoob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$', main.views.index, name='main'),
)
