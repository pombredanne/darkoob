from django.contrib import admin
from models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'sex')
	search_fields = ('user',)
	list_display = ('user', 'sex', 'birthday')

	
admin.site.register(UserProfile,UserProfileAdmin)
