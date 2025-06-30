from flask import Flask, request, jsonify
import logging
import os
import re

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('alice.log'),
        logging.StreamHandler()
    ]
)

session_storage = {}


@app.route('/', methods=['POST'])
def main():
    try:
        app.logger.info(f'Incoming request: {request.json}')

        if not validate_request(request.json):
            return jsonify({
                'response': {
                    'text': 'Произошла ошибка валидации запроса',
                    'end_session': True
                },
                'version': '1.0'
            }), 400

        response = handle_alice_request(request.json)
        app.logger.info(f'Outgoing response: {response}')
        
        return jsonify(response)

    except Exception as e:
        app.logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({
            'response': {
                'text': 'Произошла внутренняя ошибка навыка',
                'end_session': True
            },
            'version': '1.0'
        }), 500


def validate_request(req):
    return all(key in req for key in ['session', 'request', 'version'])


def handle_alice_request(req):
    user_id = req['session']['user_id']
    response = {
        'session': req['session'],
        'version': req['version'],
        'response': {
            'end_session': False,
            'buttons': []
        }
    }

    if req['session']['new']:
        init_session(user_id)
        response['response']['text'] = 'Привет! Купи слона!'
        response['response']['buttons'] = get_suggests(user_id)
        return response

    user_command = req['request']['original_utterance'].lower()
    
    if is_agreement(user_command):
        if session_storage[user_id]['current_animal'] == 'слон':
            response['response']['text'] = 'Отлично! Слона можно найти на Яндекс.Маркете! А теперь купи кролика!'
            response['response']['card'] = {
                'type': 'BigImage',
                'image_id': '1030494/46ca1d61d1e73e51b1ed',
                'title': 'Вот такого слона ты купил!',
                'description': 'Теперь купи кролика!'
            }
            session_storage[user_id]['current_animal'] = 'кролик'
            session_storage[user_id]['elephant_offers'] = 0
            response['response']['buttons'] = get_suggests(user_id)
            return response
        else:
            response['response']['text'] = 'Кролика можно найти на Яндекс.Маркете! Спасибо за покупки!'
            response['response']['end_session'] = True
            response['response']['card'] = {
                'type': 'BigImage',
                'image_id': '965417/5a10e0e4e9f435d1c5e7',
                'title': 'Вот такого кролика ты купил!',
                'description': 'Спасибо за покупки!'
            }
            return response

    session_storage[user_id]['elephant_offers'] += 1
    offer_count = session_storage[user_id]['elephant_offers']
    
    if offer_count == 1:
        response_text = f"Ну пожалуйста! Купи {session_storage[user_id]['current_animal']}а!"
    elif offer_count == 2:
        response_text = f"Ты же знаешь, как я хочу {session_storage[user_id]['current_animal']}а!"
    elif offer_count >= 3:
        response_text = f"Все говорят '{req['request']['original_utterance']}', а ты купи {session_storage[user_id]['current_animal']}а!"
    
    response['response']['text'] = response_text
    response['response']['tts'] = f"{response_text} {session_storage[user_id]['current_animal'].capitalize()} такой милый!"
    response['response']['buttons'] = get_suggests(user_id)
    
    return response


def init_session(user_id):
    session_storage[user_id] = {
        'suggests': ["Не хочу", "Не буду", "Отстань"],
        'elephant_offers': 0,
        'current_animal': 'слон'
    }


def is_agreement(text):
    agreement_patterns = [
        r'^ладно$',
        r'^куплю$',
        r'^покупаю$',
        r'^хорошо$',
        r'^да$',
        r'я\s+куплю',
        r'я\s+покупаю',
        r'я\s+согласен',
        r'я\s+согласна',
        r'я\s+хочу'
    ]
    return any(re.search(pattern, text.lower()) for pattern in agreement_patterns)


def get_suggests(user_id):
    suggests = session_storage[user_id]['suggests']
    
    buttons = [
        {'title': suggest, 'hide': True}
        for suggest in suggests[:2]
    ]
    
    session_storage[user_id]['suggests'] = suggests[1:] + [suggests[0]]
    
    buttons.append({
        'title': 'Ладно',
        'url': f"https://market.yandex.ru/search?text={session_storage[user_id]['current_animal']}",
        'hide': True
    })
    
    return buttons


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)