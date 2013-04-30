from django.contrib import admin
from models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	# list_display = ('user','sex')
	# search_fields = ('user',)
    # list_filter = ('sex',ist_display = ('user','sex')
	# search_fields = ('user',)
    # list_filter = ('sex','birthplace')'birthplace')


admin.site.register(UserProfile,UserProfileAdmin)
