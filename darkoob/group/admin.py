from django.contrib import admin
from models import Group, Schedule, Deadline

class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'admin')
    list_display = ('name', 'admin')

class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ('group', 'book', 'members')
    list_display = ('group', 'book')

class DeadlineAdmin(admin.ModelAdmin):
    search_fields = ('schedule', 'end_time')
    list_display = ('schedule', 'from_page', 'to_page', 'end_time')


admin.site.register(Group, GroupAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Deadline, DeadlineAdmin)