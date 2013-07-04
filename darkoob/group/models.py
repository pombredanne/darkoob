from django.db import models
from darkoob.social.models import User
from darkoob.book.models import Book, Quote
from django.utils import timezone
from djangoratings.fields import RatingField

class Group(models.Model):
    name = models.CharField(max_length=255)
    # comment = models.TextField(help_text=u'Description of Group') # <@vahid> i add quote instead, comment 
    admin = models.ForeignKey(User, related_name='admin_set')
    members = models.ManyToManyField(User, related_name='group_set', null=True)
    created_time = models.DateTimeField(default=timezone.now(), db_index=True)
    thumb =  models.ImageField(upload_to='groups/', null=True, blank=True)
    quote = models.ForeignKey(Quote, related_name='group_set', blank=True, null=True, help_text=u'Quote of Group')

    def __unicode__(self):
        return unicode(self.name)

class Schedule(models.Model):
    group = models.ForeignKey(Group, db_index=True)
    book = models.ForeignKey(Book, db_index=True)
    submitted_time = models.DateTimeField(default=timezone.now(), db_index=True)

    def __unicode__(self):
        return unicode("%s - %s" % (self.group.name, self.book.title))

class Deadline(models.Model):
    schedule = models.ForeignKey(Schedule)
    from_page = models.PositiveIntegerField()
    to_page = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    submitted_time = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return unicode("%s, %s from page %g to %g" % (
            self.schedule.group.name,
            self.schedule.book.title,
            self.from_page,
            self.to_page,
        ))

class Post(models.Model):
    user = models.ForeignKey(User, related_name='group_post_set')
    group = models.ForeignKey(Group)
    text = models.TextField()
    submitted_time = models.DateTimeField(default=timezone.now(), db_index=True)
    noks = RatingField(range=1, can_change_vote=True, allow_delete=True, allow_anonymous=False)

    def __unicode__(self):
        return unicode("user %s"% self.user_id)
