from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import Character
# Create your views here.


def generate_character(request):
    # TODO return a complete character as json.

    char = Character()

    html = f"<html><body>{char.stats}</body></html>"
    return JsonResponse(char.stats)
