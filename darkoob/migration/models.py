from django.db import models
from django.contrib.auth.models import User
from darkoob.book.models import Book

class Hop(models.Model):
    migration = models.ForeignKey('Migration')
    host = models.ForeignKey(User, related_name='host_set')
    received_time = models.DateTimeField(auto_now_add=True)

    def get_migration(self):
        pass

    def __unicode__(self):
        return unicode("%s - %s" % (self.migration, self.host.username))

class Migration(models.Model):
    book = models.ForeignKey(Book, related_name='book_set')
    starter = models.ForeignKey(User, related_name='starter_set')
    start_time = models.DateTimeField(auto_now_add=True)
 
    def get_user_hoped_migrations(self, user):
        '''return all migration's objects that hoped in user'''
        return [hop.migration for hop in Hop.objects.filter(host=user)]

    def get_user_host_migrations(self, user):
        '''return all migration's objects that hosted by user'''
        return [migrate for migrate in Migration.objects.filter(starter=user)]

    def get_user_related_migrations(self, user):
        '''return get_user_host_migrations() +  get_user_hoped_migrations()'''
        print self.get_user_hoped_migrations(user) + self.get_user_host_migrations(user)

    def __unicode__(self):
        return unicode("%s - %s" % (self.book.title, self.starter.username))