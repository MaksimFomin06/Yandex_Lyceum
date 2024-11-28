import sqlite3
db = "coffee.sqlite"
connect = sqlite3.connect(db)
cursor = connect.cursor()
for i in range(1, 81):
    cursor.execute(f"UPDATE coffee SET id = {4} WHERE type = 'tip_4'")

connect.commit()
connect.close()

"""
import sqlite3
db = "Lesson_16/Yandex_Homework/coffee.sqlite"
connect = sqlite3.connect(db)
cursor = connect.cursor()
for i in range(20):
    cursor.execute(f"INSERT INTO coffee(coffee_grade, degree_of_roasting, type, description, cost, packing_volume) VALUES('grade_4', 'dark', 'tip_4', 'pass', 400, '0.2')")

connect.commit()
connect.close()
"""