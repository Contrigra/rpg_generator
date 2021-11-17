from django.http import JsonResponse
from .utils import Character, get_random_name
from knave.serializers import CharacterSerializer
# Create your views here.


def generate_character(request):
    # TODO return a complete character as json.
    # TODO Traits

    char = Character()
    char = CharacterSerializer(char)

    return JsonResponse(char.data)
