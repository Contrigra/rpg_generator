from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def server_confirm(request):

    return HttpResponse('Routing confirmed')