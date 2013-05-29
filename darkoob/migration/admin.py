from django.contrib import admin
from darkoob.migration.models import Migration, Hop

class MigrationAdmin(admin.ModelAdmin):
    search_fields = ('book', 'starter', 'start_time')
    list_display = ('book', 'starter', 'start_time')

class HopAdmin(admin.ModelAdmin):
    search_fields = ('migration', 'host', 'received_time') 
    list_display = ('migration', 'host', 'received_time') 

admin.site.register(Migration, MigrationAdmin)
admin.site.register(Hop, HopAdmin)