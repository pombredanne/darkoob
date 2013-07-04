from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.db import transaction

from darkoob.book.models import Book, Review


@dajaxice_register(method='POST')
@transaction.commit_manually
def rate(request, rate, book_id):
    done = False
    book = ''
    try:
        book = Book.objects.get(id = book_id) 
        book.rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        errors.append('An error occoured in record in database')
        transaction.rollback()
    else:
        done = True
        transaction.commit()

    return simplejson.dumps({'done':done})


@dajaxice_register(method='POST')
@transaction.commit_manually
def review_rate(request, rate, review_id):
    print "review id",review_id
    done = False
    try:
        review = Review.objects.get(id=review_id)
        review.rating.add(score=rate, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        errors.append('An error occoured in record in database')
        transaction.rollback()
    else:
        done = True
        transaction.commit()

    return simplejson.dumps({'done': done})

@dajaxice_register(method='POST')
def submit_review(request, book_id, title, text):
    dajax = Dajax()
    # TODO: checks
    if len(text) < 200:
        dajax.script('''
            $.pnotify({
            title: 'Review',
            type:'error',
            text: 'Complete your review. We need some checks',
            opacity: .8
          });
          $('#id_text').val('');
          $('#id_title').val('');
        ''')    
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        pass
    else:
        Review.objects.create(book=book, user=request.user, title=title, text=text)
        dajax.script('''
            $.pnotify({
            title: 'Review',
            type:'success',
            text: 'Your review record',
            opacity: .8
          });
          $('#id_text').val('');
          $('#id_title').val('');
     
        ''')    
        #    $('#id_text').val('');
        # $('#title-look').val('');
        # $('#author-look').val('');   
    return dajax.json()



@dajaxice_register(method='POST')
def ha(request, book_name):
    print "book_name", book_name
    return simplejson.dumps({'done': True})

