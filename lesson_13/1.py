import sqlite3


def get_result(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM films WHERE genre = '1' OR genre = 25""")
    conn.commit()
    cursor.close()
    conn.close()

