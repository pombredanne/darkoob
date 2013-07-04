from django.contrib import admin
from models import Group, Schedule, Deadline, Post

class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'admin')
    list_display = ('name', 'admin')

class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ('group', 'book', 'members')
    list_display = ('group', 'book')

class DeadlineAdmin(admin.ModelAdmin):
    search_fields = ('schedule', 'end_time')
    list_display = ('schedule', 'from_page', 'to_page', 'end_time')

class PostAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('group', 'user', 'submitted_time')

admin.site.register(Group, GroupAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(Post, PostAdmin)

