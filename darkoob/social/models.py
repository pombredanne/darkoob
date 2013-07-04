from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from neomodel import StructuredNode, IntegerProperty, RelationshipTo, RelationshipFrom
from darkoob.book.models import Quote, Book

import datetime
from django.utils.timezone import utc
SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

def node():
    print "node"

User.add_to_class('node', node)

class UserNode(StructuredNode):
    user_id = IntegerProperty(required=True, index=True)
    following = RelationshipTo('UserNode', 'FOLLOW')
    followers = RelationshipFrom('UserNode', 'FOLLOW')

    def user(self):
        ''' return user object of a node '''
        return User.objects.get(id=user_id)

    def follow_person(self, user_id):
        ''' follow person that user.id=user_id'''
        followed_user = self.index.get(user_id=user_id)
        self.following.connect(followed_user, {'time': str(datetime.datetime.utcnow())})

    def is_following(self, user_id): 
        ''' return True if user in self.following.all() else False '''
        user = self.index.get(user_id=user_id)
        return True if user in self.following.all() else False

    def is_followers(self, user_id):
        ''' return True if user in self.followers.all() else False '''
        user = self.index.get(user_id=user_id)
        return True if user in self.followers.all() else False

    def get_following_list(self):
        ''' return list of all user_id that followed by this user '''
        return [user.user_id for user in self.following.all()]



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
    user = models.OneToOneField(User, db_index=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(null=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    city = models.OneToOneField(City, null=True, blank=True)
    quote = models.ForeignKey(Quote, null=True, blank=True)
    favorite_books = models.ManyToManyField(Book, null=True, blank=True)

    # for django model
    # def favorite_books(self):
    #     return ', '.join([a.title for a in self.favorite_books.all()])
    # favorite_books.short_description = "Favorite Book"

    # NOTE: userprof_obj.education_set.all() return all education set of a person 

    # def get_related_migrations(self):
    #     from darkoob.migration.models import Migration, Hop
    #     print Hop.objects.filter(host=user)

    def node(self):
        '''return node of a UserProfile'''
        return UserNode.index.get(user_id=user.id) 
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
