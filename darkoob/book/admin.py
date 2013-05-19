from django.contrib import admin
from models import Book, Publisher, Language, Author, Translator, Translation, Review

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'publisher', 'language', 'authors')
    list_display = ('title', 'publisher', 'authors')

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

class TranslatorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

class TranslationAdmin(admin.ModelAdmin):
    search_fields = ('book', 'traslator', 'language')
    list_display = ('book', 'traslator', 'language')

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('book', 'user', 'text', 'submitted_time')
    list_display = ('book', 'user', 'submitted_time')


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Review, ReviewAdmin)