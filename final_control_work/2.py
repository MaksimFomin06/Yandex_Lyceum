import csv
import json
from collections import defaultdict


def process_sounds(input_file, output_file):
    genies = defaultdict(lambda: {
        'sounds': [],
        'sources': set(),
        'durations': [],
        'volumes': []
    })
    
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='.')
        next(reader)
        for row in reader:
            if len(row) != 6:
                continue
            _, sound, volume, duration, source, genie = row
            volume = int(volume)
            duration = int(duration)
            
            genies[genie]['sounds'].append(sound)
            genies[genie]['sources'].add(source)
            genies[genie]['durations'].append(duration)
            genies[genie]['volumes'].append(volume)
    
    jsonl_lines = []
    for genie, data in genies.items():
        sounds = sorted(data['sounds'])
        sources = sorted(data['sources'])
        ave_duration = sum(data['durations']) // len(data['durations'])
        max_volume = max(data['volumes'])
        
        json_obj = {
            'name': genie,
            'sounds': sounds,
            'sources': sources,
            'ave_duration': ave_duration,
            'max_volume': max_volume
        }
        jsonl_lines.append(json.dumps(json_obj, ensure_ascii=False))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in jsonl_lines:
            f.write(line + '\n')


def main():
    process_sounds('sounds.csv', 'voices.jsonl')


if __name__ == "__main__":
    main()