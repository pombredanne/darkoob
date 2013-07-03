from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from darkoob.group.forms import GroupForm
from darkoob.group.models import Group
from darkoob.book.models import Quote
from darkoob.social.forms import NewPostForm

def group(request, group_id, slug):
    group = Group.objects.get(id=group_id, slug=slug)
    quote = Quote.get_random_quote()

    if group:
        group.admins = group.admin.admin_set.all()
        #group.members = group.members.all()

        is_member = False
        if group in request.user.group_set.all():
            is_member = True

        return render(request, "group/group_page.html", {
            'group': group,
            'quote': quote,
            'new_post_form': NewPostForm,
            'is_member': is_member,
        })
    else:
        return HttpResponse("Group Is not exist!")

@login_required
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
    groups = request.user.group_set.all()
    admin_groups = request.user.admin_set.all()
    return render(request, 'group/create_group.html', {'form': form, 'groups': groups, 'admin_groups': admin_groups })


@login_required
def members(request):
    pass

@login_required
def schedules(request):
    pass
