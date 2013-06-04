from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _

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
