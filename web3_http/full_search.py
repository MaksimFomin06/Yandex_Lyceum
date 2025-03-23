import sys
from io import BytesIO
import requests
from PIL import Image


def get_toponym_size(toponym):
    envelope = toponym['boundedBy']['Envelope']
    lower_corner = list(map(float, envelope['lowerCorner'].split()))
    upper_corner = list(map(float, envelope['upperCorner'].split()))
    return [abs(upper_corner[i] - lower_corner[i]) for i in range(2)]


def show_map(toponym, api_key="f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"):
    toponym_coordinates = toponym['Point']['pos']
    longitude, latitude = map(float, toponym_coordinates.split())
    
    size = get_toponym_size(toponym)
    
    map_params = {
        'll': f"{longitude},{latitude}",
        'spn': ','.join(map(str, size)),
        'l': 'sat',
        'pt': f"{longitude},{latitude},pm2rdm",
        'size': '600,450',
        'apikey': api_key
    }
    
    map_api_server = 'https://static-maps.yandex.ru/v1'
    response = requests.get(map_api_server, params=map_params)
    
    if response.status_code == 200:
        im = BytesIO(response.content)
        opened_image = Image.open(im)
        opened_image.show()
    else:
        print(f"Ошибка при получении карты: {response.text}")


if __name__ == "__main__":
    try:
        toponym_to_find = " ".join(sys.argv[1:])
        
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
            "geocode": toponym_to_find,
            "format": "json"
        }
        
        response = requests.get(geocoder_api_server, params=geocoder_params)
        
        if not response:
            raise Exception("Не удалось получить данные от геокодера.")
            
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        
        show_map(toponym)
        
    except Exception as e:
        print(e)