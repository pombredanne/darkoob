from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.utils.translation import ugettext as _

from models import UserProfile
from darkoob.book.models import Quote

@dajaxice_register(method='POST')
def edit_sex(request,sex):
    #TODO: In I18N should save only Male an Female in database 
    errors = []
    try:
        UserProfile.objects.filter(user=request.user).update(sex=sex)
    except:
        errors.append(_('an error occoured in saving to database'))
    else:
        done = True

    return simplejson.dumps({'done':done, 'sex':sex , 'errors':errors })

@dajaxice_register(method='POST')
def set_my_quote(request, quote_id):
    errors = []
    done = False
    message = ''
    try:
        quote = Quote.objects.get(id=quote_id)
        request.user.userprofile.quote = quote
        request.user.userprofile.save()
    except:
        errors.append(_('an error occoured in saving to database'))
    else:
        done = True
        message = 'You change your favaorite quote'

    return simplejson.dumps({'done': done, 'errors': errors, 'message': message})

def date_validators(date):
    # TODO: need to validator for date 
    errors = []
    if not (date.year > 1900 and date.year < 2030):
        errors.append('year is not valid')
    return errors

@dajaxice_register(method='POST')
def edit_birthday(request, day, year, month):
    errors = []
    done = False
    birthday = ''
    from datetime import date
    try:
        birthday = date(int(year), int(month), int(day))
        UserProfile.objects.filter(user=request.user).update(birthday=birthday)
    except: 
        errors.append(_('Please enter a valid date'))
    else: 
        done = True

    return simplejson.dumps({'done': done, 'birthday': birthday.strftime('%m/%d/%Y') , 'errors': errors})

@dajaxice_register(method='POST')
def edit_mobile(request, mobile):
    errors = []
    done = False
    try:
        UserProfile.objects.filter(user=request.user).update(mobile=mobile)
    except: 
        errors.append(_('Please enter a valid date mobile number'))
        #TODO: a phone number validator
    else: 
        done = True

    return simplejson.dumps({'done': done, 'mobile': mobile , 'errors': errors})

@dajaxice_register(method='POST')
def edit_website(request, website):
    errors = []
    print "---------------",website
    done = False
    from django.core.validators import URLValidator
    from django.core.exceptions import ValidationError
    try:
        validate = URLValidator(verify_exists=True)
        validate(website)
    except ValidationError, e:
        errors.append(_('Please enter a valid website'))
        return simplejson.dumps({'done': done, 'website': website , 'errors': errors})


    try:
        UserProfile.objects.filter(user=request.user).update(website=website)
    except: 
        errors.append(_('Cannot store to database'))
    else: 
        done = True
    return simplejson.dumps({'done': done, 'website': website , 'errors': errors})