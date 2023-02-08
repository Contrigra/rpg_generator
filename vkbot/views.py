import json
import os
import requests
from vk_api.utils import get_random_id
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .utils import get_callback_confirmation_code, get_knave_character

load_dotenv()


def vkbot(request):
    ...


redirect_url = "https://5506-94-143-197-252.ngrok.io/vk/"
client_id = "51541688"
group_id = "218492792"


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

        # TODO  1. parse text and resolve commands: 2. return a message. 3. return generated character as a message.

        case 'message_new':
            text = request_data['object']['message']['text']
            if '!knave' in text.casefold():
                # TODO construct a send message request
                # Минимум, что нужно это peer_id, причем, peer_id он и для ответа в личку и для конфы
                requests.post('https://api.vk.com/method/messages.send',
                              params=dict(
                                  peer_id=request_data['object']['message'][
                                      'peer_id'],
                                  access_token=os.environ.get(
                                      'VK_ACCESS_TOKEN'),
                                  message=get_knave_character(),
                                  random_id=get_random_id(),
                                  v=os.environ.get('VK_API_VERSION'))
                              )

                return HttpResponse('ok', content_type="text/plain")

    return HttpResponse('ok', content_type="text/plain")
