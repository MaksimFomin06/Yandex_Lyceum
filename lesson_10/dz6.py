import csv

n = int(input())
m = int(input())

data = []
with open('exam.csv', 'w', newline='', encoding='utf-8') as output_file:
    fieldnames = ['Фамилия', 'имя', 'результат 1', 'результат 2', 'результат 3', 'сумма']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    while True:
        try:
            record = input().split()
            if len(record) == 5:
                surname, name, r1, r2, r3 = record
                r1, r2, r3 = int(r1), int(r2), int(r3)
                total_score = r1 + r2 + r3
                if total_score >= n and all(score >= m for score in (r1, r2, r3)):
                    data.append({'Фамилия': surname, 'имя': name, 'результат 1': r1, 'результат 2': r2, 'результат 3': r3, 'сумма': total_score})
        except EOFError:
            break

    for student in data:
        writer.writerow(student)
