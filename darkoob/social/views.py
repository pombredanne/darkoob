from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from darkoob.social.models import UserProfile, UserNode, Post
from darkoob.social.forms import RegisterForm, ChangePasswordForm, EditProfileForm, NewPostForm

from django.template import RequestContext

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
            user = User.objects.create_user(username = cd['email'], password = cd['password'], email = cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            UserProfile.objects.filter(user = user).update(birthday = date(cd['year'], cd['month'], cd['day']))
            if cd['sex']== 'Female':
                UserProfile.objects.filter(user=user).update(sex = 'Female')
            else:
                UserProfile.objects.filter(user=user).update(sex = 'Male')
            user.save()
            return render_to_response('registered.html',{'firstname':cd['first_name']})
    else:
        #TODO: Initial return page's fields 
        form = RegisterForm( 
            # initial = {'username': 'initial'}
        )
    return render_to_response('signup.html', {'form':form})

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




    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if request.user.check_password(cd['password']):
                user = User.objects.get(username = request.user.username)
                user.set_password(cd['new_password'])
                user.save()
                return HttpResponse('Succsessfull! Password has been changed')
                #TODO: Send Email to user
            else: 
                pass
                #TODO: Raise Error('Your Password is not correct')

    else:
        form = ChangePasswordForm()
    return render_to_response('change_password.html', {'user': request.user, 'form': form})

@login_required
def home(request):
    return render(request, 'social/home.html', {'new_post_form': NewPostForm()})

@login_required
def new_post(request):
    pass

def entry_index(request,template="social/entry_index.html",page_template="social/entry_index_page.html"):
    posts = Post.objects.order_by("-submitted_time")
    count = range(1,len(posts)+1)
    # print count
    # print count[::-1]
    context = {
        'posts': posts,
        'page_template': page_template,
        'count':count[::-1],
    }
    if request.is_ajax():
        template = page_template
        # print "Ajax"
    return render_to_response(template, context,context_instance=RequestContext(request))


