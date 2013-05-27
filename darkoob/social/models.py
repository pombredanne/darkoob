from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from neomodel import StructuredNode, IntegerProperty, RelationshipTo

SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
)

class UserNode(StructuredNode):
    user_id = IntegerProperty(required=True, index=True)
    follow = RelationshipTo('UserNode', 'FOLLOW')

    def get_follows(self):
        results, metadata = self.cypher("START a=node({self}) MATCH a-[:FOLLOW]->(b) RETURN b");
        return [self.__class__.inflate(row[0]) for row in results]


    def get_followed(self):
        results, metadata = self.cypher("START a=node({self}) MATCH b-[:FOLLOW]->(a) RETURN b");
        return [self.__class__.inflate(row[0]) for row in results]

    def follow_person(self, user_id):
        import datetime
        from django.utils.timezone import utc

        followed_user = self.index.get(user_id=user_id)
        self.follow.connect(followed_user, {'time': str(datetime.datetime.utcnow().replace(tzinfo=utc))})
        self.save()

class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    submitted_time = models.DateTimeField() # TODO: Set defualt now()

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
        UserNode(user_id=instance.id).save()
        print "a node with user_id %d created!" % instance.id


post_save.connect(create_user_profile, sender=User)
