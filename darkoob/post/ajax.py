from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from darkoob.post.models import Post

@dajaxice_register(method='POST')
def nok(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.noks.add(score=1, user=request.user, ip_address=request.META['REMOTE_ADDR'])
    except:
        print "nashoda"

    print "dsf",post.noks.score
    return simplejson.dumps({'s': post.noks.votes})
