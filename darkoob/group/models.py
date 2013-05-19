from django.db import models
from darkoob.social.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User)
    members = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

