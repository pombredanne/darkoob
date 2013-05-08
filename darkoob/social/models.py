from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
SEX_CHOICES = (
        ('Male', 'Male'),
    	('Female', 'Female'),
    )
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	sex = models.CharField(max_length = 6, choices = SEX_CHOICES)
	birthday = models.DateField(null = True)
	def __unicode__(self):
		return self.user.get_full_name()

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)

post_save.connect(create_user_profile, sender = User)