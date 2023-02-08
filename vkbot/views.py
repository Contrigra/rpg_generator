import json
import os
import requests
from vk_api.utils import get_random_id
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from vkbot.utils import get_callback_confirmation_code
from knave.utils import get_knave_character_as_string

load_dotenv()


@csrf_exempt
def vk_view(request):
    request_data = json.loads(request.read())

    match request_data["type"]:
        case "confirmation":
            confirmation_code = get_callback_confirmation_code(
                access_token=os.environ.get('VK_ACCESS_TOKEN'),
                group_id=os.environ.get('VK_GROUP_ID'),
                v=os.environ.get('VK_API_VERSION'))

            return HttpResponse(confirmation_code, content_type="text/plain")

        case 'message_new':
            text = request_data['object']['message']['text']
            if '!knave' in text.casefold():
                # Минимум, что нужно помимо основных элементов это peer_id,
                # причем peer_id он и для ответа в личку и для конфы

                requests.post('https://api.vk.com/method/messages.send',
                              params=dict(
                                  peer_id=request_data['object']['message'][
                                      'peer_id'],
                                  access_token=os.environ.get(
                                      'VK_ACCESS_TOKEN'),
                                  message=get_knave_character_as_string(),
                                  random_id=get_random_id(),
                                  v=os.environ.get('VK_API_VERSION'))
                              )

                return HttpResponse('ok', content_type="text/plain")

    return HttpResponse('ok', content_type="text/plain")
