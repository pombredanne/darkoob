from django.db import models

class Migration(models.Model):
    book = models.ForeignKey(Book)
    starter = models.ForeignKey(User)
    start_time = models.DateTimeField(default=datetime.now)

    def get_migration(self):
        print self.objects.filter()

    def __unicode__(self):
        return unicode("%s - %s" % (self.book.title, self.starter.username))

class Hop(models.Model):
    migration = models.ForeignKey(Migration)
    host = models.ForeignKey(User)
    received_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return unicode("%s - %s" % (self.migration, self.host.username))
