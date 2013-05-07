from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User



def user_search_page( request ):
    return render_to_response('index_user.html',{},context_instance = RequestContext(request))

def ajax_result_of_user_search( request ):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = User.objects.filter( 
                Q( first_name__contains = q ) |
                Q( last_name__contains = q ) |
                Q( username__contains = q ) )
            return render_to_response('results_user.html',{'results':results,}, 
                                       context_instance = RequestContext(request))



    return render_to_response('results_user.html',{})