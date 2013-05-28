from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate

from darkoob.social.models import UserProfile, UserNode
from darkoob.social.forms import RegisterForm, ChangePasswordForm, EditProfileForm, NewPostForm, CommentForm
from darkoob.post.models import Post, Comment
from darkoob.book.models import Quote
from darkoob.migration.models import Migration




@login_required
def profile(request):
    form = EditProfileForm(request.POST)

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
    # # print ',,,,,,,,,,,', UserNode.index.search(user_id=27)[0]
    # a = UserNode.index.search(user_id=27)[0]
    # # print '------------', a
    # # e = UserNode(user_id=114)
    # b = UserNode.index.get(user_id=31)
    # c = UserNode.index.search(user_id=42)
    # d = UserNode.index.search(user_id=53)
    # # e = UserNode(user_id=114)
    # # e = UserNode.index.get(user_id=114)
    # # print "eeeeeeeeee",e
    # # e.save()
    # e = UserNode.index.get(user_id=114)


    # # a.follow_person(114)
    # # print b, c , d
    # # a.follow_person(114)
    # print "-----------------------------------"
    # # print b , c , d , e
    # # print 

    # for i in  a.get_followed():
    #     print i.user_id

    # # a.follow.connect(b)
    # # a.follow.connect(c)
    # # a.follow.connect(d)
    # # a[0].save()
    # print "-----------------------------------"
    # # print UserNode.index.search(user_id=26)[0].get_follows()
    # from darkoob.migration.models import Migration, Hop

    # # print Migration.objects.all()[0].hop_set.filter()
    # # print "khkh", UserProfile.objects.get(user=request.user).get_related_migrations()
    # m = Migration() 
    # print m.get_user_related_migrations(request.user)
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
    # if this is a reply to a comment, not to a post
    # if form.cleaned_data['parent_id'] != '':
    #     comment.parent = Comment.objects.get(id=request.POST['parent_id'])
    # comment.save()

    # if request.method == 'POST':
    #     form = ChangePasswordForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         if request.user.check_password(cd['password']):
    #             user = User.objects.get(username = request.user.username)
    #             user.set_password(cd['new_password'])
    #             user.save()
    #             return HttpResponse('Succsessfull! Password has been changed')
    #             #TODO: Send Email to user
    #         else: 
    #             pass
    #             #TODO: Raise Error('Your Password is not correct')

    # else:
    #     form = ChangePasswordForm()
    return render_to_response('change_password.html', {'user': request.user, 'form': form})

@login_required
def home(request):
    template = 'social/home.html'
    posts = Post.objects.order_by("-submitted_time")
    count = range(1, len(posts) + 1)

    if request.is_ajax():
        template = 'post/posts.html'

    m = Migration() 
    print m.get_user_related_migrations(request.user)

    return render(request, template, {
        'new_post_form': NewPostForm(),
        'posts': posts,
        'count': count[::-1],
        'quote': Quote.objects.order_by('?')[0],
        'migrations': m.get_user_related_migrations(request.user),
    })

@login_required
def new_post(request):
    pass

@login_required
def user_profile(request, username):
    return render(request, 'social/user_profile.html', {'username': username})

