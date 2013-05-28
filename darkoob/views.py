from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_exempt
from darkoob.social.forms import AuthenticationFormPlaceholder, RegisterForm


def index(request, **kwargs):
    error = ''
    if kwargs['errno']:
        error = "An error has occured"
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('social:home'))
    return render(request, 'index.html', {
        'signup_form': RegisterForm(),
        'login_form': AuthenticationFormPlaceholder(),
        'error': error,
    })


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

