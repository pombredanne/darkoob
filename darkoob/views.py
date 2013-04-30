from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.forms import UserCreationForm



def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('social:home'))
    return render(request, 'index.html', {'form': UserCreationForm()})


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

