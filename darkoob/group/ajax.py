from django.utils.translation import ugettext as _
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from dajax.core import Dajax
from django.db import transaction

from darkoob.migration.models import Migration, Hop
from darkoob.group.models import Group, Post
from darkoob.social.models import User



@dajaxice_register(method='POST')
def is_group_exist(request, group_name):
    status = False
    try:
        if Group.objects.filter(name=group_name):
            status = True
        else:
            status = False 
    except:
        status = False
    return simplejson.dumps({'is_exist': status})

@dajaxice_register(method='POST')
@transaction.commit_manually
def group_toggle(request, group_id, user_id, is_member):
    print is_member
    error = {}
    action_failed = ''

    user = User.objects.get(pk=user_id)
    group = Group.objects.get(pk=group_id)

    if is_member:
        try:
            group.members.remove(user)
        except Exception, e:
            print e
            action_failed = 'leave'
    else:
        try:
            group.members.add(user)
        except Exception, e:
            print e
            action_failed = 'join'

    if action_failed:
        transaction.rollback()
        error['title'] = '%s failed' % action_failed.capitalize
        error['text'] = _('A problem occured during %s, please try again.' % action_failed)
    else:
        transaction.commit()
        is_member = not is_member
    return simplejson.dumps({'error': error, 'is_member': is_member})


@dajaxice_register(method='POST')
@transaction.commit_manually
def submit_post(request, text, group_id):
    dajax = Dajax()
    post = None
    group = Group.objects.get(id=group_id)
    if text:
        post = Post.objects.create(user=request.user, text=text, group=group)
        t_rendered = render_to_string('post/post.html', {'post': post})
        dajax.prepend('#id_new_post_position', 'innerHTML', t_rendered)
        dajax.script('''
            $.pnotify({
                title: 'Sharing',
                type:'success',
                text: 'Your Post shared to group',
                opacity: .8
            });
            $('#id_text').val('');
        ''')
        transaction.commit()
        return dajax.json()
    else:
        transaction.rollback()
        #TODO: must check that user put a text in textbox or not
        pass
  
