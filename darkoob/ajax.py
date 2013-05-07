from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def dajaxice_example(request):
    return simplejson.dumps({'message':'Hello from Python!'})


@dajaxice_register
def args_example(request, text):
    return simplejson.dumps({'message':'Your message is %s!' % text})

import random
from dajax.core import Dajax

@dajaxice_register
def randomize(request):
    dajax = Dajax()
    dajax.assign('#result', 'value', random.randint(1, 10))
    return dajax.json()