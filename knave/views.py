from django.http import JsonResponse

from django.shortcuts import render
from .utils import Character
from knave.serializers import CharacterSerializer
from django.views.decorators.http import require_http_methods


def character_page(request):
    #TODO remove
    return generate_character(request)


@require_http_methods(['GET'])
def generate_character(request):

    char = Character()
    char = CharacterSerializer(char)

    return JsonResponse(char.data)
