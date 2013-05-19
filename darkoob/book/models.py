from django.db import models
from darkoob.social.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey('Publisher')
    language = models.ForeignKey('Language')
    authors = models.ManyToManyField('Author')

    def __unicode__(self):
        return unicode(self.title)

    def admin_names(self):
        return ', '.join([a.admin_name for a in self.admins.all()])
    admin_names.short_description = "Admin Names"

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Translator(models.Model):
    author = models.OneToOneField(Author)

    def __unicode__(self):
        return self.author

class Translation(models.Model):
    book = models.ForeignKey(Book)
    translator = models.ForeignKey(Translator)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.book

class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    text = models.TextField()
    submitted_time = models.DateField()

    def __unicode__(self):
        return unicode(self.book) + unicode(self.user)
