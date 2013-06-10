from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from darkoob.book.models import Book, Review


@dajaxice_register(method='POST')
def rate(request, rate, book_id):
    done = False
    book = ''
    try:
        book = Book.objects.get(id = book_id) 
        book.rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        errors.append('An error occoured in record in database')
    else:
        done = True

    return simplejson.dumps({'done':done})


@dajaxice_register(method='POST')
def review_rate(request, rate, review_id):
    done = False
    try:
        review = Review.objects.get(id=review_id)
        review.rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        errors.append('An error occoured in record in database')
    else:
        done = True

    return simplejson.dumps({'done': done})


@dajaxice_register(method='POST')
def ha(request, book_name):
    print "book_name", book_name
    return simplejson.dumps({'done': True})