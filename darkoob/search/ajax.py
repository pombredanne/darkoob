from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User

@dajaxice_register
def query(request, text):
    query = User.objects.filter(
        Q(first_name__contains = text) |
        Q(last_name__contains = text) |
        Q(username__contains = text)
    )
    
    result = dict()
    result['users'] = [u.username for u in query]
    return simplejson.dumps(result)
