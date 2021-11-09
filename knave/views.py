from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def generate_character(request):
    # TODO return a complete character as json.

    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
