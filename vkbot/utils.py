import requests


def get_callback_confirmation_code(access_token,
                                   group_id, v) -> str:
    confirmation_code = requests.get(
        'https://api.vk.com/method/groups.getCallbackConfirmationCode',
        params={'access_token': access_token, 'group_id': group_id,
                'v': v})
    confirmation_code = confirmation_code.json()['response']['code']

    return confirmation_code


def get_knave_character():
    ...

    return 'Temporary Message'
