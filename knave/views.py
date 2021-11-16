from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import Character, get_random_name
from serializers import CharacterSerializer
# Create your views here.


def generate_character(request):
    # TODO return a complete character as json.

    name = get_random_name()
    char = Character(name)
    char = CharacterSerializer(char)

    return JsonResponse(char.data)
