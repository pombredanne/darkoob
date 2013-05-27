from django.contrib import admin
from models import UserProfile, Education, School, City, Country, Post

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user', 'city', 'mobile')
    list_display = ('user', 'sex', 'birthday', 'city')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'school')
    search_fields = ('school',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    search_fields = ('name','country')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'submitted_time')
    search_fields = ('user', 'submitted_time', 'text')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
