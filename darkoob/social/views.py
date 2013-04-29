from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render(request, 'social/home.html', {})


