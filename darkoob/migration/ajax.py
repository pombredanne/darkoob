from django.utisls import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _

from darkoob.migration.models import Migration, Hop
@dajaxice_register(method='POST')
def submit_key(request,private_key):
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

    return simplejson.dumps({'done':done,'errors':errors,'message': message})