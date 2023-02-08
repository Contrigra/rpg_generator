from django.http import JsonResponse

from knave.knave_character import generate_knave_character
from knave.serializers import CharacterSerializer
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def generate_character(request):
    char = generate_knave_character()
    char = CharacterSerializer(char)

    return JsonResponse(char.data)
