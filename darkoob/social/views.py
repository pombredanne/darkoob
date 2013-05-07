from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from darkoob.social.forms import RegisterForm
from darkoob.social.models import UserProfile 

from django.core.validators import validate_email


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            import datetime
            cd = form.cleaned_data      
            email = cd['email'] #TODO: Email should be unique 
            user = User.objects.create_user(username = cd['email'], password = cd['password'], email = cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            #TODO:Change birthday model from Varchar to Data
            
            UserProfile.objects.filter(user = user).update(birthday = datetime.date(cd['year'], cd['month'], cd['day']))
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
def home(request):
	return render(request, 'social/home.html', {})

