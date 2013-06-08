from django.db import models
from darkoob.social.models import User
from darkoob.book.models import Book
from django.utils import timezone
   

class Group(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, related_name='admin_set')
    members = models.ManyToManyField(User, related_name='group_set')
    created_time = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return unicode(self.name)

class Schedule(models.Model):
    group = models.ForeignKey(Group)
    book = models.ForeignKey(Book)
    submitted_time = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return unicode("%s - %s" % (self.group.name, self.book.title))

class Deadline(models.Model):
    schedule = models.ForeignKey(Schedule)
    from_page = models.PositiveIntegerField()
    to_page = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return unicode("%s, %s from page %g to %g" % (
            self.schedule.group.name,
            self.schedule.book.title,
            self.from_page,
            self.to_page,
        ))

