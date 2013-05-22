from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
)

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.OneToOneField(Country)

    def __unicode__(self):
        return self.name 

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    birthday = models.DateField(null=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    city = models.OneToOneField(City, null=True, blank=True)

    # NOTE: userprof_obj.education_set.all() return all education set of a person 

    def __unicode__(self):
        return self.user.get_full_name()

class School(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name 

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='education_set')
    school = models.OneToOneField(School)

    def __unicode__(self):
        return unicode(self.school)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
