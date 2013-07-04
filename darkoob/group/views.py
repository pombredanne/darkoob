from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db import transaction

from darkoob.group.forms import GroupForm
from darkoob.group.models import Group
from darkoob.book.models import Quote
from darkoob.social.forms import NewPostForm
from darkoob.group.models import Post

def group(request, group_id, group_slug):
    template = 'group/group_page.html'

    group = Group.objects.get(id=group_id)
    quote = Quote.get_random_quote()
    if request.is_ajax():
        template = 'post/posts.html'

    if group and group_slug.lower() == '-'.join(group.name.lower().split()):
        group.admins = group.admin.admin_set.all()
        #group.members = group.members.all()

        is_member = False
        if group in request.user.group_set.all():
            is_member = True

        posts = Post.objects.filter(group=group).order_by("-submitted_time").all()
        return render(request, template, {
            'group': group,
            'posts': posts,
            'quote': quote,
            'new_post_form': NewPostForm,
            'is_member': is_member,
        })

    else:
        return HttpResponse("Group Is not exist!")

@login_required
@transaction.commit_manually
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not request.user.userprofile.quote:
                group = Group(name=cd['name'], admin=request.user)
            else:
                group = Group(name=cd['name'], admin=request.user, quote=request.user.userprofile.quote)
            group.save()
            for member in cd['members'].strip(',').split(','):
                try:
                    user = User.objects.get(username=member)
                    group.members.add(user)
                except:
                    pass
            group.save()
    else:
        form = GroupForm()
        transaction.rollback()

    groups = request.user.group_set.all()
    admin_groups = request.user.admin_set.all()
    transaction.commit()
    return render(request, 'group/create_group.html', {'form': form, 'groups': groups, 'admin_groups': admin_groups })


@login_required
def members(request):
    pass

@login_required
def schedules(request):
    pass
