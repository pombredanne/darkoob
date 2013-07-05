from django.conf.urls import patterns, include, url
from darkoob.group import views as group_view
from darkoob.social import views as social_view

urlpatterns = patterns('',
    url(r'^(?P<group_id>\d+)/(?P<group_slug>[-\w]+)/$', group_view.group, name='group_page'),
    url(r'^new/$', group_view.create_group, name='create_group'),
    url(r'^look/$', social_view.user_lookup),
    url(r'^members/$', group_view.members, name='members'),
    url(r'^schedules/$', group_view.schedules, name='schedules'),
    url(r'^(?P<group_id>\d+)/(?P<group_slug>[-\w]+)/add-schedule/$', group_view.add_schedule, name='add_schedule'),
    # url(r'^rate/$', book_views.rate, name='rate'),

)
