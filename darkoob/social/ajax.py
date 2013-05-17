from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register(method='POST')
def sex(request,day):
	errors = []
	message = 'salam'
	print 'day:', day

	# try:
	# 	UserProfile.objects.filter(user=request.user).update(about=about)
	# except:
	# 	print "nashod"
	# 	message="False"
	# else:
	# 	message="True"
	return simplejson.dumps({"message":message,"day":day,'errors':errors})

