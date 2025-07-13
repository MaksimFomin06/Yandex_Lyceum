import os
import json
import random
import zipfile


def process_orders():
    os.makedirs('result', exist_ok=True)
    
    encode_data = []
    
    for filename in os.listdir('orders'):
        if not filename.endswith('.json'):
            continue
            
        filepath = os.path.join('orders', filename)
        
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue
        
        personal_data = {}
        for field in ['name', 'address', 'phone']:
            if field in data:
                personal_data[field] = data.pop(field)
        
        person_id = random.randint(10**6, 10**9 - 1)
        data['personID'] = person_id
        
        if personal_data:
            personal_data['personID'] = person_id
            encode_data.append(personal_data)
        
        with open(os.path.join('result', filename), 'w') as f:
            json.dump(data, f, indent=2)
    
    with open(os.path.join('result', 'encode.json'), 'w') as f:
        json.dump(encode_data, f, indent=2)
    
    with zipfile.ZipFile('result.zip', 'w') as zipf:
        for root, _, files in os.walk('result'):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)
    
    import shutil
    shutil.rmtree('result')


if __name__ == '__main__':
    if not os.path.exists('orders'):
        print("Ошибка: папка 'orders' не найдена!")
    else:
        process_orders()