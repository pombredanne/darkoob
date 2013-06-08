from django.contrib import admin
from darkoob.post.models import Post, GroupPostStream, CommentStream, ProfilePostStream

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'submitted_time')
    search_fields = ('user', 'submitted_time', 'text')

class GroupPostStreamAdmin(admin.ModelAdmin):
    list_display = ('group', 'post')
    search_fields = ('group', 'post')

class CommentStreamAdmin(admin.ModelAdmin):
    list_display = ('post', 'parent')
    search_fields = ('post',)

class ProfilePostStreamAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(GroupPostStream, GroupPostStreamAdmin)
admin.site.register(CommentStream, CommentStreamAdmin)
admin.site.register(ProfilePostStream, ProfilePostStreamAdmin)
