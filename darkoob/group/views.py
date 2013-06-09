from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from darkoob.group.forms import GroupForm
from darkoob.group.models import Group

def group(request, group_id, group_name):
    group = Group.objects.get(id=group_id, name=group_name)

    if group:
        group.admins = group.admin.admin_set.all()
        group.members = group.members.all()
        for i in group.members:
            print i
        return render(request, "group/group_page.html" ,{'group': group})
    else:
        return HttpResponse("Group Is not exist!")

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Group(name=cd['name'], admin=request.user).save()
    else:
        form = GroupForm()
    return render(request, 'group/create_group.html', {'form': form })


