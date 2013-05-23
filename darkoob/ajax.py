from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.db.models import Q
from django.contrib.auth.models import User

@dajaxice_register
def dajaxice_example(request):
    return simplejson.dumps({'message':'Hello from Python!'})


@dajaxice_register
def args_example(request, text):
#    return simplejson.dumps({'message':'Your message is %s!' % text,
#                             'users': [1, 2, 3]
#                            })
    query = User.objects.filter(
        Q(first_name__contains = text) |
        Q(last_name__contains = text) |
        Q(username__contains = text)
    )
    
    result = dict()
    result['users'] = [(u.username, u.email) for u in query]
    return simplejson.dumps(result)

import random
from dajax.core import Dajax

@dajaxice_register
def randomize(request):
    dajax = Dajax()
    dajax.assign('#result', 'value', random.randint(1, 10))
    return dajax.json()

#@dajaxice_register
#def search(request, text):
#    query = User.objects.filter(
#        Q(first_name__contains = text) |
#        Q(last_name__contains = text) |
#        Q(username__contains = text)
#    )
#    
#    result = dict()
#    result['users'] = [u.username for u in query]
#    return simplejson.dumps(result)
