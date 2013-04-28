from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_exempt


from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

def HomePage(request):
    return HttpResponse("HELLO DARKOOB! :D")


def BasicPage(request):
	return render_to_response('index.html', {})


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

