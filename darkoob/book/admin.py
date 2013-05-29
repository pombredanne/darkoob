from django.contrib import admin
from models import Book, Publisher, Language, Author, Translator, Translation, Review, Quote

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'publisher', 'language', 'authors')
    list_display = ('title', 'publisher', 'author_names')

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
    search_fields = ('author',)
    list_display = ('author',)

class TranslationAdmin(admin.ModelAdmin):
    search_fields = ('book', 'translator', 'language')
    list_display = ('book', 'translator', 'language')

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('book', 'user', 'text', 'submitted_time')
    list_display = ('book', 'user', 'submitted_time')

class QuoteAdmin(admin.ModelAdmin):
    search_fields = ('author', 'text', 'book') 
    list_display = ('author', 'text', 'book')

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Quote, QuoteAdmin)