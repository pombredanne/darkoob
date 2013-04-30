from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from darkoob.social.forms import RegisterForm

def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data      
        email=cd["email"]
#TODO:check email to isnt in db,email should be unique 
        if cd["pw"]==cd["pwconfirm"]:
            user=User.objects.create_user(username=cd["email"],password=cd["pw"],email=cd["email"])
            user.first_name =cd["first_name"]
            user.last_name=cd["last_name"]
        print dir(user)

        print UserProfile.objects.filter(user=user).update(birthday=str(cd["year"]) + " "+ str(cd["month"]) + " " + str(cd["day"]))
        if cd["sex"]=="Female":
            UserProfile.objects.filter(user=user).update(src='female.jpg')
            UserProfile.objects.filter(user=user).update(sex=False)
        else:
            UserProfile.objects.filter(user=user).update(src='male.jpg')
            

        user.save()

        return render_to_response('registered.html',{'firstname':cd['firstname']})
    else:
        form = RegisterForm(
            initial={'username': 'I love your site!'}
        )
    return render_to_response('signup.html', {'form': form})



    # if request.method != 'POST':
    #     return render(request, 'signup.html', {
    #         'errors': [_('an internal error has happend.')]
    #     })
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     username = request.POST['username']
    #     password = request.POST['password1']
    #     user = User.objects.create_user(username=username, password=password)
    #     return HttpResponseRedirect(reverse('social:login'))


@login_required
def home(request):
	return render(request, 'social/home.html', {})

