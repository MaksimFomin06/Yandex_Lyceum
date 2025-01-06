import csv


def get_specialties(min_percent):
    with open('vps.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        result = []
        for row in reader:
            if float(row['соответствует в %']) >= min_percent:
                result.append(row['Специальность'])
        return result


if __name__ == "__main__":
    min_percent = float(input().strip())
    specialties = get_specialties(min_percent)
    for specialty in specialties:
        print(specialty)