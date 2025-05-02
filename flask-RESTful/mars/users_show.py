from flask import render_template, Blueprint, abort
from data import db_session
from data.users import User
import requests

blueprint = Blueprint('users_show', __name__)


@blueprint.route('/users_show/<int:user_id>')
def show_user_city(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    
    if not user or not user.city_from:
        abort(404)

    geocoder_api_key = "8013b162-6b42-4997-9691-77b7074026e0"
    geocoder_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={geocoder_api_key}&format=json&geocode={user.city_from}"
    
    try:
        response = requests.get(geocoder_url)
        data = response.json()
        pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = pos.split()
    except:
        abort(500)
    
    return render_template('user_city.html', 
                         user=user,
                         lat=lat,
                         lon=lon,
                         yandex_maps_api_key="8013b162-6b42-4997-9691-77b7074026e0")