from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from darkoob.social import views as social_views

urlpatterns = patterns('',
    url(r'^home/', social_views.home, name='home'),
    url(r'^signup/$', social_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'social/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^change_password/$', social_views.change_password, name = 'change_password')
)
