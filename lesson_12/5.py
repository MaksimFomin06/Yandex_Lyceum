import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""SELECT id from genres 
                   WHERE title = 'боевик'""")
    rows = cursor.fetchone()
    boevik_genre_id = rows[0]
    cursor.execute(f"""
                   DELETE FROM films
                   WHERE genre = {boevik_genre_id}
                   AND duration >= 90
                   """)
    connect.commit()
    cursor.close()
    connect.close()
