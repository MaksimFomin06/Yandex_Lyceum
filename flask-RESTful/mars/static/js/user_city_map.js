document.addEventListener('DOMContentLoaded', function() {
    const mapElement = document.getElementById('map');
    const lat = parseFloat(mapElement.dataset.lat);
    const lon = parseFloat(mapElement.dataset.lon);
    const city = mapElement.dataset.city;
    const userName = mapElement.dataset.userName;
    const apiKey = mapElement.dataset.apiKey;

    const script = document.createElement('script');
    script.src = `https://api-maps.yandex.ru/2.1/?apikey=${apiKey}&lang=ru_RU&onload=initMap`;
    script.async = true;
    
    window.initMap = function() {
        ymaps.ready(function() {
            const map = new ymaps.Map("map", {
                center: [lat, lon],
                zoom: 12,
                controls: ['zoomControl']
            });
            
            const placemark = new ymaps.Placemark([lat, lon], {
                hintContent: city,
                balloonContent: `Родной город ${userName}`
            }, {
                preset: 'islands#blueHomeIcon'
            });
            
            map.geoObjects.add(placemark);
            map.behaviors.disable('scrollZoom');
            placemark.balloon.open();
        });
    };

    document.head.appendChild(script);
});