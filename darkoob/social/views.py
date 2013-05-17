from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from darkoob.social.forms import RegisterForm, ChangePasswordForm

from django.contrib.auth.models import User
from darkoob.social.models import UserProfile 

@login_required
def profile(request):

    # print request.user.userprofile.Education.all()
    # print dir(request.user.userprofile)
    return render_to_response('profile.html',{'user': request.user})

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
	return render(request, 'social/home.html', {})

