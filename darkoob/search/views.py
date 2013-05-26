from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import User

import re



def search_user( request ):
    return render_to_response('search_user.html', {}, context_instance = RequestContext(request))

def search_user_result( request ):
    query_string = ''
    found_entries = None
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            query_string = request.GET['q']
            print 'query_string:',query_string
            entry_query = get_query(query_string,['first_name','last_name','username'] )
            print 'entry_query:',entry_query
            results = User.objects.filter(entry_query)
            print "results", results
            return render_to_response(
                'search_user_result.html',
                {'results':results,}, 
                context_instance = RequestContext(request),
            )
    return render_to_response('search_user_result.html', {})


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """
    Splits the query string in invidual keywords, getting rid of unecessary spaces
    and grouping quoted words together.
    Example:
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
