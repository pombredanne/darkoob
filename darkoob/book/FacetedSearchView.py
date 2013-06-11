from django.conf.urls.defaults import *
from haystack.query import SearchQuerySet
from haystack.view import FacetedSearchView
from haystack.form import FacetedSearchForm

sqs = SearchQuerySet().facet('authors')

urlpattern = patterns(
    'haystack.view',
    url(
        r'^$',
        FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), 
        name='haystack_search'
    ),
)

