from flask import Flask, jsonify
import csv
import sqlite3

app = Flask(__name__)

def get_words_for_genie(genie_name):
    genie_words = set()
    with open('named.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) >= 3 and row[2].lower() == genie_name.lower():
                genie_words.add(row[1])
    
    if not genie_words:
        return []
    
    conn = sqlite3.connect('judgments.db')
    cursor = conn.cursor()
    
    placeholders = ','.join(['?'] * len(genie_words))
    query = f"""
    SELECT w.word, m.value 
    FROM Words w
    JOIN Means m ON w.judge_id = m.id
    WHERE w.word IN ({placeholders})
    ORDER BY m.value ASC, w.word ASC
    """
    
    cursor.execute(query, list(genie_words))
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        return []
    
    if len(results) <= 5:
        return [row[0] for row in results]
    
    fifth_value = results[4][1]
    output_words = []
    for row in results:
        if row[1] <= fifth_value:
            output_words.append(row[0])
        else:
            break
    
    return output_words

@app.route('/oath/<genie>/')
def get_genie_words(genie):
    words = get_words_for_genie(genie)
    return jsonify(words)

if __name__ == '__main__':
    app.run(port=8080)