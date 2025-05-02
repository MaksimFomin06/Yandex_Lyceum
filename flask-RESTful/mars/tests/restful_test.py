from requests import get, post, delete

print(get("http://localhost:5000/api/v2/users").json())

print(get("http://localhost:5000/api/v2/users/2").json())

print(get("http://localhost:5000/api/v2/users/999").json())

print(get("http://localhost:5000/api/v2/users/abc").json())

print(post("http://localhost:5000/api/v2/users", json={
    'surname': 'Ivanov',
    'name': 'Ivan',
    'age': 25,
    'position': 'developer',
    'speciality': 'IT',
    'address': 'Moscow',
    'email': 'ivan@mail.ru',
    'city_from': 'Moscow',
    'password': '1234'
}).json())

print(post("http://localhost:5000/api/v2/users", json={
    'name': 'Ivan',
    'position': 'developer'
}).json())

print(delete(f"http://localhost:5000/api/v2/users/1").json())

print(delete(f"http://localhost:5000/api/v2/users/9999999").json())