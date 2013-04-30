from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from darkoob.social.forms import RegisterForm
from darkoob.social.models import UserProfile 

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data      
        email = cd['email'] #TODO: mail should be unique 

        if cd['password']==cd['confirm_password']:
            user=User.objects.create_user(username=cd['email'], password = cd['pw'], email = cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
	#######TODO: change this part
        #TODO:Change birthday model from Varchar to Data
        UserProfile.objects.filter(user=user).update(birthday=str(cd['year']) + ' '+ str(cd['month']) + ' ' + str(cd['day']))
        if cd['sex']=='Female':
            UserProfile.objects.filter(user=user).update(sex = 'Female')
        else:
            UserProfile.objects.filter(user=user).update(sex = 'Male')
	########
        user.save()
        return render_to_response('registered.html',{'firstname':cd['first_name']})
    else:
        #TODO: initial return page field 
        form = RegisterForm( 
            initial = {'username': 'initial'}
        )
    return render_to_response('signup.html', {'form': form})


@login_required
def home(request):
	return render(request, 'social/home.html', {})

