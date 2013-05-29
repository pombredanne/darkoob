from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from darkoob.group.models import Group

def group(request, group_id, group_name):
    group = Group.objects.get(id = group_id)#, name = group_name)

    if group:
        return render(request, "group/group_page.html" ,{'group_id': group_id})
    else:
        return HttpResponse("Group Is not exist!")