from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _

from darkoob.migration.models import Migration, Hop
from darkoob.group.models import Group


@dajaxice_register(method='POST')
def is_group_exist(request, group_name):
    status = True
    try:
        print Group.objects.filter(name=group_name)
    except:
        status = False
    else:
        status = True
    return simplejson.dumps({'is_exist': status})