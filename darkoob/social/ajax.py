from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register(method='POST')
def edit_sex(request,sex):
	errors = []
	done = False
	print 'day:', sex
	return simplejson.dumps({'done': done, 'sex': sex, 'errors': errors})

