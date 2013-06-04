from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.utils import timezone

from darkoob.social.models import UserProfile, UserNode
from darkoob.social.forms import RegisterForm, ChangePasswordForm, EditProfileForm, NewPostForm, CommentForm
from darkoob.post.models import Post, Comment
from darkoob.book.models import Quote
from darkoob.migration.models import Migration
from darkoob.group.models import Schedule






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
    # print ',,,,,,,,,,,', UserNode.index.search(user_id=27)[0]
    a = UserNode.index.get(user_id=200)
    # print '------------', a
    b = UserNode.index.get(user_id=201)
    c = UserNode.index.get(user_id=202)
    print a, b , c
    # a.save()
    # b.save()

    # d = UserNode.index.search(user_id=53)
    # e = UserNode(user_id=114)
    # e = UserNode.index.get(user_id=114)
    # print "eeeeeeeeee",e
    # e.save()
    # e = UserNode.index.get(user_id=114)


    a.follow_person(201)
    # b.follow_person
    print a.get_followers(), a.get_following()
    # print b, c , d
    # a.follow_person(114)
    print "-----------------------------------"
    # print b , c , d , e
    # print 

    # for i in  a.get_followed():
        # print i.user_id

    # a.follow.connect(b)
    # a.follow.connect(c)
    # a.follow.connect(d)
    # a[0].save()
    print "-----------------------------------"
    # print UserNode.index.search(user_id=26)[0].get_follows()
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
    groups = request.user.group_set.all()
    admin_groups = request.user.admin_set.all()
    book_deadlines = []
    # for group in admin_groups:
    #     for schedule in group.schedule_set.all():
    #         deadline_set = schedule.deadline_set.all()
    #         for i in range(len(deadline_set)):
    #             deadline_set[i].time_percentage = (timezone.now() - deadline_set[i].start_time).total_seconds()  / (deadline_set[i].end_time - deadline_set[i].start_time).total_seconds() * 100
    #         book_deadlines.append([ schedule.book , deadline_set])
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

    return render(request, template, {
        'new_post_form': NewPostForm(),
        'posts': posts,
        'count': count[::-1],
        'groups': groups,
        'admin_groups': admin_groups,
        'book_deadlines': book_deadlines,
        'quote': Quote.objects.order_by('?')[0],
        'migrations': m.get_user_related_migrations(request.user),
    })

@login_required
def following(request):
    '''A view for showing all following users of logged in user'''

    template = 'social/following.html'
    user_node = UserNode.index.get(user_id=request.user.id)
    following = [User.objects.get(id=node.user_id) for node in user_node.following.all()]
    count = range(1, len(following) + 1)
    print following

    if request.is_ajax():
        template = 'social/following_page.html'

    return render(request, template, {
        'following': following,
        'count': count[::-1],
    })

@login_required
def followers(request):
    '''A view for showing all followers users of logged in user'''
    
    # start cleanup code 
    template = 'social/followers.html'
    user_node = UserNode.index.get(user_id=request.user.id)
    followers = [User.objects.get(id=node.user_id) for node in user_node.followers.all()]
    count = range(1, len(followers) + 1)
    print followers

    if request.is_ajax():
        template = 'social/followers_page.html'

    return render(request, template, {
        'followers': followers,
        'count': count[::-1],
    })
    # end cleanup code 

    # Dont remove plese. I know it's very dirty:D 

    # template = 'social/followers.html'
    # posts = Post.objects.order_by("-submitted_time")
    # count = range(1, len(posts) + 1)
    # a = UserNode.index.get(user_id=request.user.id)
    # b = UserNode.index.get(user_id=2)
    # c = UserNode.index.get(user_id=3)

    # print a,b,c
    # a.follow.connect(c)

    # a.save()
    # print 'find', UserNode.index.search(user_id=request.user.id)[0].get_following()
    # print 'saladsm',UserNode.index.get(user_id=request.user.id).get_followers()
    # u1 = UserNode.index.get(user_id=1)
    # u1 = UserNode.index.get(user_id=2)

    # u1 = UserNode(user_id=1).save()
    # u2 = UserNode(user_id=5).save()
    # u3 = UserNode(user_id=6).save()


    # u1.follow_person(2)
    # u2.follow_person(1)
    # u1.follow_person(3)
    # u3.follow_person(1)
    # UserNode(user_id=3).save()
    # UserNode(user_id=4).save()

    
    # u1.follow_person(2)
    # u1.follow_person(5)
    # u1.follow_person(6)
    # print [User.objects.get(id=node.user_id) for node in u1.following.all()]
    # # print type(u1.followers.all())
    # print "User 1 follows {}".format(u1.following.all())
    # print "User 1's followers {}".format(u1.followers.all())
    # print "User 1 follows {}".format(u1.get_following())
    # print "User 1's followers {}".format(u1.get_followers())
    # u1 = UserNode(user_id=2).save()
    # u2 = UserNode(user_id=3).save()
    # u3 = UserNode(user_id=4).save()
    # u4 = UserNode(user_id=5).save()

    # u.follow_person(2)
    # u.follow_person(3)
    # u.follow_person(4)
    # u.follow_person(5)
    # print ")))))))((((((())))(((("
    # print u.followers
    # print u.following
    # for i in u.get_following():
        # print "i", dir(i)

    # print "User 1 follows {}".format(u.get_following())
    # print "User 1's followers {}".format(u.get_followers())

    # if request.is_ajax():
    #     template = 'post/posts.html'


    # return render(request, template, {
    #     'posts': posts,
    #     'count': count[::-1],
    # })

@login_required
def new_post(request):
    pass

@login_required
def user_profile(request, username):
    return render(request, 'social/user_profile.html', {'username': username})


# 
