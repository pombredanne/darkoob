from django.db import models
from darkoob.social.models import User
from taggit.managers import TaggableManager
from djangoratings.fields import RatingField
from datetime import datetime    

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey('Publisher')
    language = models.ForeignKey('Language')
    authors = models.ManyToManyField('Author')
    tags = TaggableManager()
    rating = RatingField(range = 5, can_change_vote = True, allow_delete = False, allow_anonymous = False )
    
    def author_names(self):
        return ', '.join([a.name for a in self.authors.all()])
    author_names.short_description = "Author Names"

    def __unicode__(self):
        return unicode(self.title)

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
        return unicode(self.author)

class Translation(models.Model):
    book = models.ForeignKey(Book)
    translator = models.ForeignKey(Translator)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return unicode(self.book)

class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    text = models.TextField()
    submitted_time = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return unicode(self.book) + unicode(self.user)

class Quote(models.Model):
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book, null=True)
    text = models.TextField()

    def __unicode__(self):
        return unicode(self.text)

class Migration(models.Model):
    book = models.ForeignKey(Book)
    starter = models.ForeignKey(User)
    start_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return unicode("%s - %s" % (self.book.title, self.starter.username))

class Hop(models.Model):
    migration = models.ForeignKey(Migration)
    host = models.ForeignKey(User)
    received_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return unicode("%s - %s" % (self.migration, self.host.username))
