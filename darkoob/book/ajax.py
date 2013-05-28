from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from darkoob.book.models import Book 


@dajaxice_register(method='POST')
def rate(request, rate, book_id):
    done = True#False
    errors = []
    #try:
    Book.objects.filter(id = book_id).rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    #except:
    #     errors.append('dsfds')
    # else:
    #     done = True


    return simplejson.dumps({'done':done})

