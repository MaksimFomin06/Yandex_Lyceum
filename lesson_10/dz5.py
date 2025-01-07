import csv


def main():
    federal_district = input("Название федерального округа: ").strip()
    start_year = int(input("Начальный год: "))
    end_year = int(input("Конечный год: "))

    # Проверка допустимости года
    if start_year < 2015 or start_year > 2019 or end_year < 2015 or end_year > 2019 or start_year >= end_year:
        print("Некорректные годы")
        return

    subjects = []

    with open('salary.csv', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=';')
        for row in reader:
            if row['Федеральный округ'] == federal_district:
                start_salary = int(row[str(start_year)])
                end_salary = int(row[str(end_year)])
                growth_rate = (end_salary - start_salary) / start_salary * 100
                if growth_rate < 4:
                    subjects.append((row['Субъект'], start_year, end_year))

    with open('out_file.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerow(['Субъект', str(start_year), str(end_year)])
        for subject in subjects:
            writer.writerow(subject)


if __name__ == "__main__":
    main()