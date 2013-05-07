from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User



def index_user( request ):
    return render_to_response('index_user.html',{},context_instance = RequestContext(request))
