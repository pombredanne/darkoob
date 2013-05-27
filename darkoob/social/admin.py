from django.contrib import admin
from models import UserProfile, Education, School, City, Country

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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
