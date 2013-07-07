from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _
from django.db import transaction

from darkoob.migration.models import Migration, Hop
from darkoob.book.models import Book

@dajaxice_register(method='POST')
def submit_key(request, private_key):
    errors = []
    done = True
    message = ''
    try:
        migration = Migration.objects.get(private_key=private_key)
    except:
        done = False
        errors.append(_('Invalid private key'))
    else:
        if migration.starter == request.user:
            done = False
            errors.append(_('you are starter of this book migration!'))
        else:
            try:
                hop = Hop.objects.get(migration=migration, host=request.user)
            except:
                Hop.objects.create(migration=migration, host=request.user)
                done = True
                message = _('thanks for record %s book,' % migration.book.title )
            else:
                errors.append(_('You have already submitted this book'))
                done = False

    return simplejson.dumps({'done': done, 'errors': errors, 'message': message})

@dajaxice_register(method='POST')
@transaction.commit_manually
def key(request, private_key):
    errors = []
    done = True
    message = ''
    try:
        migration = Migration.objects.get(private_key=private_key)
    except:
        done = False
        errors.append(_('Invalid private key'))
    else:
        if migration.starter == request.user:
            done = False
            errors.append(_('you are starter of this book migration!'))
            transaction.rollback()
        else:
            try:
                hop = Hop.objects.get(migration=migration, host=request.user)
            except:
                Hop.objects.create(migration=migration, host=request.user)
                done = True
                message = _('thanks for record %s book,' % migration.book.title )
                transaction.commit()
            else:
                errors.append(_('You have already submitted this book'))
                done = False
                transaction.rollback()

    return simplejson.dumps({'done': done, 'errors': errors, 'message': message})

import random
import string 
def generate_private_key(len=10):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(len))

@dajaxice_register(method='POST')
def submit_new_migration_form(request, book_id, message):
    done = True
    try:
        book = Book.objects.get(id=book_id)
    except:
        private_key = ''
        book = ''            
        transaction.rollback()
    else:
        private_key = generate_private_key()
        Migration.objects.create(book=book, starter=request.user,
            starter_message=message, private_key=private_key
        )
        transaction.commit()

    return simplejson.dumps({'done': done, 'private_key': private_key, 'book': book.title})



# @dajaxice_register(method='POST')
# def submit_start_new_migration(request, book_name):
#     errors = []
#     done = True
#     print "salam"
#     # try:
#     #     Book.objects.get(title=book_name)
#     # except:
#     #     print "salam"
#     # else:
#     #     pass


#     return simplejson.dumps({'done': done, 'errors': errors})
@dajaxice_register(method='POST')
def is_book(request, book_title):
    try:
        Book.objects.get(title=book_title)
    except:
        result = False
    else:
        result = True
    print 'ajax result', result
    return simplejson.dumps({'done': True, 'result': result })


