import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import vk_api

load_dotenv()


def vkbot(request):
    ...


@csrf_exempt
def server_confirm(request):


    return HttpResponse('464cc8db', content_type="text/plain")
