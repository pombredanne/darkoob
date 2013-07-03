from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q

from darkoob.social.models import UserProfile, UserNode
from darkoob.social.forms import RegisterForm, ChangePasswordForm, EditProfileForm, NewPostForm, CommentForm
from darkoob.post.models import Post, Comment
from darkoob.book.models import Quote
from darkoob.migration.models import Migration
from darkoob.group.models import Schedule
from django.utils import simplejson

from avatar.forms import PrimaryAvatarForm, DeleteAvatarForm
# from avatar.models import Avatar
from avatar.templatetags import avatar_tags

def test(user):
    from darkoob.book.models import Author
    from datetime import date

    vahid = Author.objects.create(name='vahid')
    quote = []
    users = []
    for i in range(2,15):
        q = Quote.objects.create(author=vahid, text='I love %d person, I think ...'%i, user=user)
        quote.append(q)
    for i in range(2,10):
        print i
        user = User.objects.create_user(username='user%d'%i, password = 'password', email ='email@yahoo.com')
        user.first_name = 'user-%d-name'%i
        user.last_name = 'user-%d-family'%i
        UserProfile.objects.filter(user=user).update(birthday=date(1993, 4, 5))
        if i%2:
            UserProfile.objects.filter(user=user).update(mobile='09381442622')
            UserProfile.objects.filter(user=user).update(sex = 'Female')
        else:
            UserProfile.objects.filter(user=user).update(quote=quote[i])
            UserProfile.objects.filter(user=user).update(sex ='Male')
        user.save()
        users.append(user)
    from random import randint
    for i in range(1,9):
        print i
        random =[]
        numbers = randint(5,6)
        for j in range(numbers):
            a = randint(2,9)
            if a not in random:
                random.append(a)
        main = UserNode.index.get(user_id=i)
        for k in random:
            main.follow_person(k)
   

@login_required
def profile(request):
    form = EditProfileForm(request.POST)
    # test(request.user)
    return render_to_response('social/profile.html',{'user': request.user, 'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            from datetime import date
            cd = form.cleaned_data      
            email = cd['email'] #TODO: Email should be unique 
            user = User.objects.create_user(username = email, password = cd['password'], email = cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            UserProfile.objects.filter(user = user).update(birthday = date(cd['year'], cd['month'], cd['day']))
            if cd['sex'] == 'Female':
                UserProfile.objects.filter(user=user).update(sex = 'Female')
            else:
                UserProfile.objects.filter(user=user).update(sex = 'Male')
            user.save()
            # u = authenticate(email, cd['password'])
            # return HttpResponseRedirect(reverse('social:home'))
            return render_to_response('registered.html',{'firstname':cd['first_name']})
        else:
            return HttpResponseRedirect(reverse('index'))

    elif request.method == 'GET':
        #TODO: Initial return page's fields 
        form = RegisterForm( 
            # initial = {'username': 'initial'}
        )
        return render_to_response('signup.html', {'form':form})
    else:
        return HttpResponseRedirect(reverse('index'))

@login_required
def change_password(request):
    ##
    ## Please Dont remove:D
    ##
    a = UserNode.index.get(user_id=request.user.id)
    print a
    a.get_following_list()
    # print "User 1 follows {}".format(a.following.all())
    # print "User 1's followers {}".format(a.followers.all())

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            comment = Comment(
                author=request.POST['author'],
                comment=request.POST['comment'],
            )
            if form.cleaned_data['parent_id'] != '':
                comment.parent = Comment.objects.get(id=request.POST['parent_id'])
            comment.save()
    else:
        form = CommentForm()
    return render_to_response('change_password.html', {'user': request.user, 'form': form})

@login_required
def home(request):
    template = 'social/home.html'

    #TODO: if two import fixed i should move them to top of page
    from itertools import chain
    import operator

    posts = Post.objects.order_by("-submitted_time")
    quotes = Quote.objects.order_by("-submitted_time")
    thing = list(chain(posts, quotes))
    thing = sorted(thing, key=operator.attrgetter('submitted_time'), reverse=True)
    count = range(1, len(thing) + 1) 

    groups = request.user.group_set.all()
    admin_groups = request.user.admin_set.all()
    book_deadlines = []
    for group in admin_groups:
        for schedule in group.schedule_set.all():
            deadline_set = schedule.deadline_set.all()
            for i in range(len(deadline_set)):
                deadline_set[i].time_percentage = (timezone.now() - deadline_set[i].start_time).total_seconds()  / (deadline_set[i].end_time - deadline_set[i].start_time).total_seconds() * 100
            book_deadlines.append([ schedule.book , deadline_set])
    for group in groups:
        for schedule in group.schedule_set.all():
            deadline_set = schedule.deadline_set.all()
            for i in range(len(deadline_set)):
                deadline_set[i].time_percentage = (timezone.now() - deadline_set[i].start_time).total_seconds()  / (deadline_set[i].end_time - deadline_set[i].start_time).total_seconds() * 100

            book_deadlines.append([ schedule.book , deadline_set])
        
    if request.is_ajax():
        template = 'post/posts.html'

    m = Migration() 
    # print m.get_user_related_migrations(request.user)

    # Todo: Change this part
    suggestion_list = list(User.objects.order_by('?')[0:4])    # TODO : ISSUE #54

    quote = Quote.get_random_quote()

    return render(request, template, {
        'new_post_form': NewPostForm(),
        'posts': thing,
        'count': count[::-1],
        'groups': groups,
        'admin_groups': admin_groups,
        'book_deadlines': book_deadlines,
        'quote': quote,
        'migrations': m.get_user_related_migrations(request.user),
        'suggestion_list': suggestion_list,
    })


@login_required
def following(request):
    '''A view for showing all following users of logged in user'''

    template = 'social/following.html'
    user_node = UserNode.index.get(user_id=request.user.id)
    following = [User.objects.get(id=node.user_id) for node in user_node.following.all()]
    count = range(1, len(following) + 1)

    request_user_following_list = user_node.get_following_list()
 
    if request.is_ajax():
        template = 'social/person_bar_page.html'

    return render(request, template, {
        'persons': following,
        'request_user_following_list': request_user_following_list,
        'count': count[::-1],
    })

@login_required
def followers(request):
    '''A view for showing all followers users of logged in user'''
    
    template = 'social/followers.html'
    user_node = UserNode.index.get(user_id=request.user.id)
    followers = [User.objects.get(id=node.user_id) for node in user_node.followers.all()]
    count = range(1, len(followers) + 1)

    request_user_following_list = user_node.get_following_list()

    if request.is_ajax():
        template = 'social/person_bar_page.html'

    return render(request, template, {
        'persons': followers,
        'request_user_following_list': request_user_following_list,
        'count': count[::-1],
    })



@login_required
def new_post(request):
    pass

@login_required
def user_profile(request, username):
    template = 'social/user_profile.html'

    try:
        user = User.objects.get(username=username)
        groups = user.group_set.all()
        admin_groups = user.admin_set.all()
    except:
        pass
        #raise 404

    try:
        user_node = UserNode.index.get(user_id=request.user.id)
        is_following = user_node.is_following(user.id)
        is_followers = user_node.is_followers(user.id)      
    except:
        is_following = False
        is_followers = False

    if request.is_ajax():
        template = 'post/posts.html'
    favorite_books = user.userprofile.favorite_books.all()
    m = Migration() 

    posts = Post.objects.filter(user=user).order_by("-submitted_time")
    count = range(1, len(posts) + 1)
    return render(request, template,
        {
            'person_object': user,
            'is_following': is_following,
            'is_followers': is_followers,
            'groups': groups,
            'admin_groups':admin_groups,
            'posts': posts,
            'count': count,
            'favorite_books': favorite_books,
            'migrations': m.get_user_related_migrations(User.objects.get(username=username)),
        }
    )
 
@login_required
def user_favorite_books(request, username):
    template = 'social/user_favorite_books.html'
    user = User.objects.get(username=username)
    favorite_books = user.userprofile.favorite_books.all()
    count = range(1, len(favorite_books) + 1)

    try:
        user_node = UserNode.index.get(user_id=request.user.id)
        is_following = user_node.is_following(user.id)
        is_followers = user_node.is_followers(user.id)      
    except:
        is_following = False
        is_followers = False

    if request.is_ajax():
        template = 'social/favorite_books_page.html'

    request_user_favorite_books_list = request.user.userprofile.favorite_books.all()

    return render(request, template, {
        'person_object': user,
        'is_following': is_following,
        'is_followers': is_followers,
        'request_user_favorite_books_list': request_user_favorite_books_list,
        'favorite_books': favorite_books,
        'count': count[::-1],
    })
@login_required
def favorite_books(request):
    template = 'social/favorite_books.html'
    favorite_books = request.user.userprofile.favorite_books.all()
    count = range(1, len(favorite_books) + 1)

    if request.is_ajax():
        if request.META.get('HTTP_X_PJAX', 'false') == 'true':
            pass
        template = 'social/favorite_books_page.html'

    request_user_favorite_books_list = request.user.userprofile.favorite_books.all()
    
    return render(request, template, {
        'person_object': request.user,
        'favorite_books': favorite_books,
        'request_user_favorite_books_list': request_user_favorite_books_list,
        'count': count[::-1],
    })

@login_required
def user_following(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404
    else:           
        template = 'social/user_following.html'
        user_node = UserNode.index.get(user_id=user.id)
        following = [User.objects.get(id=node.user_id) for node in user_node.following.all()]
        count = range(1, len(following) + 1)

        request_user_following_list = UserNode.index.get(user_id=request.user.id).get_following_list()

        if request.is_ajax():
            template = 'social/person_bar_page.html'

        try:
            user_node = UserNode.index.get(user_id=request.user.id)
            is_following = user_node.is_following(user.id)
            is_followers = user_node.is_followers(user.id)      
        except:
            is_following = False
            is_followers = False

        return render(request, template, {
            'person_object': user,
            'persons': following,
            'is_following': is_following,
            'is_followers': is_followers,
            'request_user_following_list': request_user_following_list,
            'count': count[::-1],
        })
        return render(request, 'social/user_profile.html', {'username': username})

@login_required
def user_followers(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404
    else:
        template = 'social/user_followers.html'
        user_node = UserNode.index.get(user_id=user.id)
        followers = [User.objects.get(id=node.user_id) for node in user_node.followers.all()]
        count = range(1, len(followers) + 1)

        request_user_following_list = UserNode.index.get(user_id=request.user.id).get_following_list()

        if request.is_ajax():
            template = 'social/person_bar_page.html'

        try:
            user_node = UserNode.index.get(user_id=request.user.id)
            is_following = user_node.is_following(user.id)
            is_followers = user_node.is_followers(user.id)      
        except:
            is_following = False
            is_followers = False

        return render(request, template, {
            'person_object': user,
            'persons': followers,
            'is_following': is_following,
            'is_followers': is_followers,
            'request_user_following_list': request_user_following_list,
            'count': count[::-1],
        })

        return render(request, 'social/user_profile.html', {'username': username})

def user_lookup(request):
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            model_results = User.objects.filter(
                Q(first_name__icontains=value) |
                Q(last_name__icontains=value) |
                Q(username__icontains=value)
            )
            results = [ {'username': x.username , 'photo': avatar_tags.avatar_url(x,30), 'full_name': x.get_full_name()}  for x in model_results]
    to_json = []
    jt=simplejson.dumps(results)
    return HttpResponse(jt, mimetype='application/json')
