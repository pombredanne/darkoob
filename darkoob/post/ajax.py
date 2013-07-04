from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.db import transaction

from darkoob.post.models import Post

@dajaxice_register(method='POST')
@transaction.commit_manually
def nok(request, post_id):
    ok = True
    try:
        post = Post.objects.get(id=post_id)
        post.noks.add(score=1, user=request.user, ip_address=request.META['REMOTE_ADDR'])
        transaction.commit()
    except:
        ok = False
        trasaction.rollback()

    return simplejson.dumps({'pid': post_id, 'ok': ok, 'noks': str(post.noks.votes)})
