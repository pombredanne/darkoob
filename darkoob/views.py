from django.http import HttpResponse
from django.shortcuts import render_to_response

def HomePage(request):
    return HttpResponse("HELLO DARKOOB! :D")


def BasicPage(request):
	return render_to_response('index.html', {})
