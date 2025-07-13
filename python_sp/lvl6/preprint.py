import zipfile
import os
import re


def extract_annotations():
    if not os.path.exists('arxiv.zip'):
        print("Ошибка: файл arxiv.zip не найден!")
        return

    with zipfile.ZipFile('arxiv.zip', 'r') as zip_ref:
        file_list = sorted([f for f in zip_ref.namelist() if f.lower().endswith('.txt')])
        
        if not file_list:
            print("Ошибка: в архиве нет .txt файлов!")
            return

        annotations = []
        
        for filename in file_list:
            with zip_ref.open(filename) as file:
                content = file.read().decode('utf-8')
                
                lines = [line.strip() for line in content.split('\n') if line.strip()]
                
                if len(lines) < 3:
                    print(f"Предупреждение: в файле {filename} меньше 3 строк, пропускаем")
                    continue
                
                title = lines[0]
                authors = lines[1]
                
                abstract_start = 2
                if len(lines) > 2 and re.fullmatch(r'abstract', lines[2], re.IGNORECASE):
                    abstract_start = 3
                
                if len(lines) <= abstract_start:
                    print(f"Предупреждение: в файле {filename} нет аннотации, пропускаем")
                    continue
                
                abstract = lines[abstract_start]
                first_sentence = re.split(r'(?<=[.!?])\s+', abstract)[0]
                annotations.append(f"{title}\n{authors}\n{first_sentence}")
        
        with open('annotations.txt', 'w', encoding='utf-8') as out_file:
            out_file.write('\n\n'.join(annotations))


extract_annotations()