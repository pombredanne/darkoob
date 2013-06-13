from django.utils import simplejson
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax

from darkoob.social.models import UserProfile, UserNode
from django.contrib.auth.models import User
from darkoob.social.models import UserProfile
from darkoob.book.models import Quote, Book, Author
from darkoob.post.models import Post
from avatar.templatetags import avatar_tags


@dajaxice_register(method='POST')
def star_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        request.user.userprofile.favorite_books.add(book)
    except:
        done = False
    else:
        done = True
    return simplejson.dumps({'done': done, 'book_id': book_id})

@dajaxice_register(method='POST')
def follow_person(request, user_id):
    try:
        user = UserNode.index.get(user_id=request.user.id)
        user.follow_person(user_id)
    except:
        done = False
    else:
        done = True
    return simplejson.dumps({'done': done, 'user_id': user_id})
    
# @dajaxice_register(method='POST')
# def follow_request(request, following_id):
#     # TODO : ISSUE #54
#     try:
#         user = UserNode.index.get(user_id=request.user.id)
#         user.follow_person(following_id)
#         done = True 
#     except:
#         print "nashhod"
#         done = False
#     return simplejson.dumps({'done':done})

@dajaxice_register(method='POST')
def get_quote(request):
    dajax = Dajax()
    quote = Quote.get_random_quote()
    detail = quote.author.name 
    if quote.book:
        detail += ' (' + quote.book.title + ')'
    dajax.assign('#quote_text', 'innerHTML', quote.text)
    dajax.assign('#quote_detail', 'innerHTML', detail)
    dajax.script("$('#random_quote').attr('quote_id','%d')"%quote.id)
 
    return dajax.json()

@dajaxice_register(method='POST')
def submit_post(request, text, type, author, book):
    dajax = Dajax()
    post = None

    if type == '0':
        # post type
        post = Post.objects.create(user_id=request.user, text=text)
        t_rendered = render_to_string('post/post.html', {'post': post})
        dajax.append('#id_new_post_position', 'innerHTML', t_rendered)
        dajax.clear('#id_text', 'value')

    if type == '1':
        # qoute type
        try: 
            author = Author.objects.get(name=author)
        except Author.DoesNotExist:
            #TODO: Check user reputation and error error if user score less than ?
            author = Author.objects.create(name=author)

        try:
            book = Book.objects.get(title=book)
        except Book.DoesNotExist:
            #TODO: Check user reputation and error error if user score less than ?
            Quote.objects.create(user=request.user, text=text, author=author)
        else:
            Quote.objects.create(user=request.user, text=text, book=book) # set author, book  
        dajax.script('''
            $.pnotify({
            title: 'Sharing',
            type:'success',
            text: 'your comment shared',
            opacity: .8
          });
            $('#id_text').val('');
            $('#title-look').val('');
            $('#author-look').val('');
        ''')
        
    if type == '2':
        # deadline type 
        pass


    return dajax.json()
    # return simplejson.dumps({'done': True, 'post': 'df'})

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
        quote = Quote.objects.get(id=int(quote_id))
        UserProfile.objects.filter(user=request.user).update(quote=quote)
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
def is_user(request, username):
    try:
        user = User.objects.get(username=username)
        if user:
            return simplejson.dumps({'is_exist': True, 'url': avatar_tags.avatar_url(user,40), 'full_name': user.get_full_name()})
    except:
        return simplejson.dumps({'is_exist': False})
@dajaxice_register(method='POST')
def edit_website(request, website):
    errors = []
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
