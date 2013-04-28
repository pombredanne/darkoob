from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darkoob.views.home', name='home'),
    # url(r'^darkoob/', include('darkoob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$', 'darkoob.main.views.index'),
)
