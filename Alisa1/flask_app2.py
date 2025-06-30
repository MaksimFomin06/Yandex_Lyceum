import json


def handler(event, context):
    print("Event: " + str(event))
    
    req = json.loads(event['body'])
    
    response = {
        'session': req['session'],
        'version': req['version'],
        'response': {
            'end_session': False
        }
    }
    
    handle_dialog(req, response)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


def handle_dialog(req, res):
    user_id = req['session']['user_id']
    
    if req['session']['new']:
        res['response']['text'] = 'Привет! Купи слона!'
        res['response']['buttons'] = [
            {"title": "Не хочу", "hide": True},
            {"title": "Не буду", "hide": True},
            {"title": "Отстань", "hide": True}
        ]
        return
    
    if req['request']['original_utterance'].lower() in ['ладно', 'куплю', 'покупаю', 'хорошо']:
        res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
        res['response']['end_session'] = True
        return
    
    res['response']['text'] = f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
    res['response']['buttons'] = [
        {"title": "Ладно", "url": "https://market.yandex.ru/search?text=слон", "hide": True},
        {"title": "Не хочу", "hide": True}
    ]