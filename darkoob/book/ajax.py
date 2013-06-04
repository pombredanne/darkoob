from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from darkoob.book.models import Book 


@dajaxice_register(method='POST')
def rate(request, rate, book_id):
    done = False
    errors = []
    book = ''
    try:
        book = Book.objects.get(id = book_id) 
        book.rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        errors.append('An error occoured in record in database')
    else:
        try: 
            rate = book.rating.get_rating()
        except:
            errors.append('An error occoured in reading rate')
            rate = 0
        done = True


    return simplejson.dumps({'done':done , 'rate':rate, 'errors': errors })

@dajaxice_register(method='POST')
def ha(request, book_name):
    print "book_name", book_name
    return simplejson.dumps({'done': True})