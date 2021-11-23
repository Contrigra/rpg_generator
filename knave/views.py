from django.http import JsonResponse
from .utils import Character
from knave.serializers import CharacterSerializer


# Create your views here.


def generate_character(request):
    # TODO return a complete character as json.

    char = Character()
    char = CharacterSerializer(char)

    return JsonResponse(char.data)
