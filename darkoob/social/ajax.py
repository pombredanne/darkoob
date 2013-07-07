from django.utils import simplejson
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.db import transaction
from django.contrib.auth.models import User

from darkoob.social.models import UserProfile, UserNode
from darkoob.social.models import UserProfile
from darkoob.book.models import Quote, Book, Author
from darkoob.post.models import Post
from avatar.templatetags import avatar_tags


@dajaxice_register(method='POST')
@transaction.commit_manually
def star_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        request.user.userprofile.favorite_books.add(book)
    except:
        done = False
        transaction.rollback()
    else:
        done = True
        transaction.commit()
    return simplejson.dumps({'done': done, 'book_id': book_id})

@dajaxice_register(method='POST')
@transaction.commit_manually
def follow_person(request, user_id):
    try:
        user = UserNode.index.get(user_id=request.user.id)
        user.follow_person(user_id)
    except:
        done = False
        transaction.rollback()
    else:
        done = True
        transaction.commit()
    return simplejson.dumps({'done': done, 'user_id': user_id})

@dajaxice_register(method='POST')
def get_quote(request):
    dajax = Dajax()
    quote = Quote.get_random_quote()
    detail = quote.author.name
    if quote.book:
        detail += ' (' + quote.book.title + ')'
    dajax.assign('#quote-text', 'innerHTML', quote.text)
    dajax.assign('#quote-details', 'innerHTML', detail)
    dajax.script("$('#top-quote blockquote').attr('quote-id','%d')" % quote.id)
 
    return dajax.json()

#@dajaxice_register(method='GET')
#def submit_post(request, text, type, author, book):
    #print 'type', type
    #print 'text', text
    #print 'author', author
    #print 'book', book




@dajaxice_register(method='POST')
def submit_post(request, text, type, author, book):
    dajax = Dajax()
    post = None
    if type == '0':
        if text:
            post = Post.objects.create(user=request.user, text=text)
            t_rendered = render_to_string('post/post.html', {'post': post})
            dajax.prepend('#id_new_post_position', 'innerHTML', t_rendered)
            dajax.script('''
                $.pnotify({
                title: 'Successful',
                type:'success',
                text: 'Your post has been submitted.',
                opacity: .8
              });
                $('#id_text').val('');
            ''')  
        else:
            print "text doesn't exists"
            dajax.script('''
                         $.pnotify({
                         title: 'Error',
                         type:'error',
                         text: 'Post text is empty!',
                         opacity: .8
                        });
                         $('#id_text').val('');
                         ''')
    elif type == '1':
        print 'type1', type
        # qoute type
        if text:
            print "text is", text
            try: 
                author = Author.objects.get(name=author)
            except Author.DoesNotExist:
                #TODO: Check user reputation and error error if user score less than ?
                author = Author.objects.create(name=author)

            try:
                book = Book.objects.get(title=book)
            except Book.DoesNotExist:
                #TODO: Check user reputation and error error if user score less than ?
                quote = Quote.objects.create(user=request.user, text=text, author=author)
            else:
                quote = Quote.objects.create(user=request.user, text=text, book=book) # set author, book  


            t_rendered = render_to_string('post/post.html', {'post': quote})
            dajax.prepend('#id_new_post_position', 'innerHTML', t_rendered)
            dajax.script('''
                $.pnotify({
                title: 'Successful',
                type:'success',
                text: 'Your quote has been shared.',
                opacity: .8
              });
                $('#id_text').val('');
                $('#title-look').val('');
                $('#author-look').val('');
            ''')        
        else:
            print "text doesn't exists"
            dajax.script('''
                         $.pnotify({
                         title: 'Error',
                         type:'error',
                         text: 'Quote is empty!',
                         opacity: .8
                        });
                         $('#id_text').val('');
                         ''')  
    return dajax.json()

@dajaxice_register(method='POST')
@transaction.commit_manually
def edit_gender(request,gender):
    #TODO: In I18N should save only Male an Female in database 
    errors = []
    try:
        UserProfile.objects.filter(user=request.user).update(gender=gender)
    except:
        errors.append(_('an error occoured in saving to database'))
        transaction.rollback() 
    else:
        transaction.commit() 
        done = True

    return simplejson.dumps({'done':done, 'gender':gender , 'errors':errors })

@dajaxice_register(method='POST')
def sex(request, sex):
    dajax = Dajax()
    if sex=='Male':
        UserProfile.objects.filter(user=request.user).update(sex='M')
    else:
        UserProfile.objects.filter(user=request.user).update(sex='F')

    dajax.script('''
         $.pnotify({
         title: 'Quote',
         type:'success',
         text: 'your Sex Updated',
         opacity: .8
        });
    ''') 
    return dajax.json()

@dajaxice_register(method='POST')
def edit_birthday(request, day, year, month):
    print "month", month
    print "day", day
    print "year", year
    from datetime import date
    dajax = Dajax()

    try:
        birthday = date(int(year), int(month), int(day))
    except:
        dajax.script('''
            $.pnotify({
            type:'error',
            text: 'Please enter a valid date',
            opacity: .8
            });
        ''')
    else:
        dajax.script('''
            $.pnotify({
            title: 'Quote',
            type:'success',
            text: 'your Birthday Updated',
            opacity: .8
            });
        ''')

    # UserProfile.objects.filter(user=request.user).update(birthday=birthday)

     
    return dajax.json()



@dajaxice_register(method='POST')
@transaction.commit_manually
def set_my_quote(request, quote_id):
    errors = []
    done = False
    message = ''
    try:
        quote = Quote.objects.get(id=int(quote_id))
        UserProfile.objects.filter(user=request.user).update(quote=quote)
    except:
        errors.append(_('an error occoured in saving to database'))
        transaction.rollback()
    else:
        done = True
        message = 'You change your favaorite quote'
        transaction.commit()

    return simplejson.dumps({'done': done, 'errors': errors, 'message': message})

def date_validators(date):
    # TODO: need to validator for date 
    errors = []
    if not (date.year > 1900 and date.year < 2030):
        errors.append('year is not valid')
        return errors

# @dajaxice_register(method='POST')
# @transaction.commit_manually
# def edit_birthday(request, day, year, month):
#     errors = []
#     done = False
#     birthday = ''
#     from datetime import date
#     try:
#         birthday = date(int(year), int(month), int(day))
#         UserProfile.objects.filter(user=request.user).update(birthday=birthday)
#     except: 
#         errors.append(_('Please enter a valid date'))
#         transaction.rollback()
#     else: 
#         done = True
#         transaction.commit()

#     return simplejson.dumps({'done': done, 'birthday': birthday.strftime('%m/%d/%Y') , 'errors': errors})

@dajaxice_register(method='POST')
@transaction.commit_manually
def edit_mobile(request, mobile):
    errors = []
    done = False
    try:
        UserProfile.objects.filter(user=request.user).update(mobile=mobile)
    except: 
        errors.append(_('Please enter a valid date mobile number'))
        #TODO: a phone number validator
        transaction.rollback()
    else: 
        done = True
        transaction.commit()

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
@transaction.commit_manually
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
        transaction.rollback()
        return simplejson.dumps({'done': done, 'website': website , 'errors': errors})


    try:
        UserProfile.objects.filter(user=request.user).update(website=website)
    except: 
        errors.append(_('Cannot store to database'))
        transaction.rollback()
    else: 
        done = True
        transaction.commit()

    return simplejson.dumps({'done': done, 'website': website , 'errors': errors})
