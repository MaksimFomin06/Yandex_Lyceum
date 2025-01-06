import csv


def main():
    plants = []
    
    while True:
        try:
            input_line = input()
            if not input_line.strip():  
                break
            plants.append(input_line.split('\t'))
        except EOFError:
            break
    
    fieldnames = ['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']
    with open('plantis.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for plant in plants:
            writer.writerow({
                'nomen': plant[0],
                'definitio': plant[1],
                'pluma': plant[2],
                'Russian nomen': plant[3],
                'familia': plant[4],
                'Russian nomen familia': plant[5]
            })


if __name__ == "__main__":
    main()