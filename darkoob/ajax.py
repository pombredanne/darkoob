from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def dajaxice_example(request):
    return simplejson.dumps({'message':'Hello from Python!'})


@dajaxice_register
def args_example(request, text):
    return simplejson.dumps({'message':'Your message is %s!' % text})