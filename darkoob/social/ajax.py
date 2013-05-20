from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from models import UserProfile

@dajaxice_register(method='POST')
def edit_sex(request, sex):
	errors = []

    # try:
    #     UserProfile.objects.filter(user=request.user).update(sex=sex)
    # except:
    #     errors.append('An error ecoured while change information')
    # else:
    #     done = True
	# print 'day:',sex
    done = True
	return simplejson.dumps({'done': done,'sex': 'Male', 'errors': errors})

