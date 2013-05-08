from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User



def search_user( request ):
    return render_to_response('search_user.html', {}, context_instance = RequestContext(request))

def search_user_result( request ):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = User.objects.filter( 
                Q(first_name__contains = q) |
                Q(last_name__contains = q) |
                Q(username__contains = q))
            return render_to_response(
                                    'search_user_result.html',
                                    {'results':results,}, 
                                    context_instance = RequestContext(request),
                                    )
    return render_to_response('search_user_result.html', {})