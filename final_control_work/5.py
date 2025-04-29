from flask import Flask, jsonify
import csv
import sqlite3
from collections import defaultdict

app = Flask(__name__)

genie_words = defaultdict(list)

with open('named.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        if len(row) >= 3:
            genie_words[row[2].lower()].append(row[1])


def get_db_connection():
    conn = sqlite3.connect('judgments.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/oath/<genie>/')
def get_words(genie):
    genie_lower = genie.lower()
    if genie_lower not in genie_words:
        return "[]"
    
    words = genie_words[genie_lower]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT w.word, m.value 
    FROM Words w
    JOIN Means m ON w.judge_id = m.id
    WHERE w.word IN ({})
    ORDER BY m.value ASC, w.word ASC
    """.format(','.join(['?'] * len(words)))
    
    cursor.execute(query, words)
    evaluated_words = cursor.fetchall()
    conn.close()
    
    sorted_words = sorted(evaluated_words, key=lambda x: (x['value'], x['word']))
    
    if not sorted_words:
        return "[]"
    
    result_words = [item['word'] for item in sorted_words[:5]]
    
    if len(sorted_words) > 5:
        fifth_value = sorted_words[4]['value']
        
        for item in sorted_words[5:]:
            if item['value'] == fifth_value:
                result_words.append(item['word'])
            else:
                break
    
    return jsonify(result_words)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)