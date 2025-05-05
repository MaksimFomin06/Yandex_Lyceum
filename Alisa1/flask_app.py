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
        session_storage[user_id] = {
            'suggests': ["Не хочу", "Не буду", "Отстань"],
            'elephant_offers': 0
        }
        response['response']['text'] = 'Привет! Купи слона!'
        response['response']['buttons'] = get_suggests(user_id)
        return response

    user_command = req['request']['original_utterance'].lower()
    
    if is_agreement(user_command):
        response['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
        response['response']['end_session'] = True
        response['response']['card'] = {
            'type': 'BigImage',
            'image_id': '1030494/46ca1d61d1e73e51b1ed',
            'title': 'Вот такого слона ты можешь купить!',
            'description': 'Загляни на Яндекс.Маркет'
        }
        return response

    session_storage[user_id]['elephant_offers'] += 1
    offer_count = session_storage[user_id]['elephant_offers']
    
    if offer_count == 1:
        response_text = "Ну пожалуйста! Купи слона!"
    elif offer_count == 2:
        response_text = "Ты же знаешь, как я хочу слона!"
    elif offer_count >= 3:
        response_text = f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
    
    response['response']['text'] = response_text
    response['response']['tts'] = f"{response_text} Сло+ник такой милый!"
    response['response']['buttons'] = get_suggests(user_id)
    
    return response


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
        'url': 'https://market.yandex.ru/search?text=слон',
        'hide': True
    })
    
    return buttons


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)