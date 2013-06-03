from django.db import models
from darkoob.social.models import User
from darkoob.group.models import Group
from django.utils import timezone  

from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
	user_id = models.ForeignKey(User, related_name='post_user_id_set')
	text = models.TextField()
	submitted_time = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return unicode(self.text)


class Comment(MPTTModel):
    """ Threaded comments for blog posts """
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=60)
    comment = models.TextField()
    added  = models.DateTimeField(default=timezone.now())
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['added']


class GroupPostStream(models.Model):
	group_id = models.ForeignKey(Group)
	post_id = models.ForeignKey(Post)

	def __unicode__(self):
		return unicode("group_id: %d    post_id: %d"%(self.group_id, self.post_id))

class CommentStream(models.Model):
	post_id = models.ForeignKey(Post)
	parent_id = models.ForeignKey(Post, related_name='comment_stream_parent_id_set')

	def __unicode__(self):
		return unicode("Comment with post_id: %d comes for Post with id: %s"%(self.post_id, parent_id))

class ProfilePostStream(models.Model):
	user_id = models.ForeignKey(User, related_name='profile_post_stream_user_id_set')
	post_id = models.ForeignKey(Post)

	def __unicode__(self):
		return unicode("Post with id: %d belong to user with id: %d"%(self.post_id, self.user_id))