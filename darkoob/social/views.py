from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method != 'POST':
        return render(request, 'index.html', {
            'errors': [_('an internal error has happend.')]
        })
    form = UserCreationForm(request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password1']
        user = User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect(reverse('social:login'))


@login_required
def home(request):
	return render(request, 'social/home.html', {})

