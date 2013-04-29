# Create your views here.
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _

def index(request):
    return render_to_response('main/index.html', {})
