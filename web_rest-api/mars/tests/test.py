from requests import delete, get, post, put
"""
#print(get('http://localhost:5000/api/jobs').json())

#print(get('http://localhost:5000/api/jobs/2').json())

#print(get('http://localhost:5000/api/jobs/7985635948').json())

#print(get('http://localhost:5000/api/jobs/djfhs').json())

#Пытается отправить пустой запрос
print(post("http://localhost:5000/api/jobs", json={}).json())

#Добавляет работу в бд
print(post("http://localhost:5000/api/jobs", 
           json={"team_leader": 1,
                 "job": "работа добавленная через POST",
                 "work_size": 21,
                 "collaborators": "Тест"}).json())

#Пытается отправить некорректный запрос

print(post("http://localhost:5000/api/jobs", 
           json={"team_leader": 1,
                 "work_size": 21,
                 "collaborators": "Тест"}).json())

print(delete("http://localhost:5000/api/jobs/8"))

print(delete("http://localhost:5000/api/jobs/sdfsd"))

print(get("http://localhost:5000/api/jobs/sdfsd").json())
 
print(put("http://localhost:5000/api/jobs/3", 
           json={"job": "работа измененная через PATCH"}).json())
print(put("http://localhost:5000/api/jobs/hb", 
           json={"job": "работа измененная через PATCH"}).json())

print(put("http://localhost:5000/api/jobs/3", 
           json={"jobbbbb": "работа измененная через PATCH"}).json())

print(get("http://localhost:5000/api/jobs").json())
"""