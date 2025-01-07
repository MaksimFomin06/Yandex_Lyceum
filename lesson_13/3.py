import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
                   UPDATE films
                   SET duration = duration * 2
                   WHERE genre = 8 OR genre = 32
                   """)
    connect.commit()
    cursor.close()
    connect.close()