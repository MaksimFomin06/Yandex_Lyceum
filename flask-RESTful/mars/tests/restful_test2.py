from requests import get, post, delete, put

print(get("http://localhost:5000/api/v2/jobs").json())

print(get("http://localhost:5000/api/v2/jobs/1").json())

print(get("http://localhost:5000/api/v2/jobs/999").json())

print(post("http://localhost:5000/api/v2/jobs", json={
    'team_leader': 1,
    'job': 'Разработка мобильного приложения',
    'work_size': 20,
    'collaborators': '2,3',
    'is_finished': False
}).json())

print(post("http://localhost:5000/api/v2/jobs", json={
    'team_leader': 1,
    'job': 'Битая вакансия',
    'collaborators': '1'
}).json())

print(put("http://localhost:5000/api/v2/jobs/1", json={
    'team_leader': 1,
    'job': 'Обновленное описание',
    'work_size': 35,
    'collaborators': '1,2,3',
    'is_finished': True
}).json())

print(delete(f"http://localhost:5000/api/v2/jobs/1").json())

print(delete("http://localhost:5000/api/v2/jobs/999").json())