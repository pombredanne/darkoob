from django.conf.urls import patterns, include, url
from darkoob.migration import views as migration_views

urlpatterns = patterns('',
    url(r'^migration/new$', migration_views.start_new_migration, name='new_migration'),
)
