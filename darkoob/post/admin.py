from django.contrib import admin
from models import Post, GroupPostStream, CommentStream, ProfilePostStream

class PostAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'submitted_time')
    search_fields = ('user_id', 'submitted_time', 'text')

class GroupPostStreamAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'post_id')
    search_fields = ('group_id', 'post_id')

class CommentStreamAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'parent_id')
    search_fields = ('post_id',)

class ProfilePostStreamAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post_id')
    search_fields = ('user_id', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(GroupPostStream, GroupPostStreamAdmin)
admin.site.register(CommentStream, CommentStreamAdmin)
admin.site.register(ProfilePostStream, ProfilePostStreamAdmin)