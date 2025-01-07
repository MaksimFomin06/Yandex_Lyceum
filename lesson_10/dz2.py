import csv

# Функция для сортировки участников по баллу и фамилии
def sort_participants(participants):
    return sorted(participants, key=lambda x: (-int(x['Score']), x['surname']))

def clean_user_name(user_name):
    # Удалить первый символ "У" и следующие 4 цифры
    cleaned_name = user_name[6:]
    
    # Оставляем только фамилию
    parts = cleaned_name.strip('"').split()
    surname = parts[-1].strip(',')
    
    return surname

def main():
    with open('rez.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        school_number, class_number = map(int, input().split())
        
        participants = []
        
        for row in reader:
            login = row['login']
            
            if f'sh-kaluga16-{school_number}-{class_number}' in login:
                surname = clean_user_name(row['user_name'])
                score = row['Score'].split('(')[0]
                
                participants.append({
                    'surname': surname,
                    'Score': score
                })
    
    sorted_participants = sort_participants(participants)
    
    for participant in sorted_participants:
        print(f"{participant['surname']} {participant['Score']}")

if __name__ == "__main__":
    main()