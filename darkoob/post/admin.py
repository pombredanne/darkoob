from django.contrib import admin
from darkoob.post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'submitted_time')
    search_fields = ('user', 'submitted_time', 'text')



admin.site.register(Post, PostAdmin)

