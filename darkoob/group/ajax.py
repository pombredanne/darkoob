from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _

from darkoob.migration.models import Migration, Hop
from darkoob.group.models import Group
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
        error['title'] = '%s failed' % action_failed.capitalize
        error['text'] = _('A problem occured during %s, please try again.' % action_failed)
    else:
        is_member = not is_member
    return simplejson.dumps({'error': error, 'is_member': is_member})
