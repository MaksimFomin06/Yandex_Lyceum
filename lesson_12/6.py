import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
                   SELECT id FROM genres
                   WHERE title = 'мюзикл'
                   """)
    rows = cursor.fetchone()
    musikl_genre_id = rows[0]

    cursor.execute(f"""
                   UPDATE films
                   SET duration = 100
                   WHERE genre = {musikl_genre_id}
                   AND duration > 100
                   """)
    connect.commit()
    cursor.close()
    connect.close()
