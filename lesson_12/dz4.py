import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
                   SELECT id FROM genres
                   WHERE title = 'фантастика'
                   """)
    rows = cursor.fetchone()
    fantastic_films_id = rows[0]

    cursor.execute(f"""
                   DELETE FROM films
                   WHERE genre = {fantastic_films_id}
                   AND year < 2000
                   AND duration > 90
                   """)
    connect.commit()
    cursor.close()
    connect.close()