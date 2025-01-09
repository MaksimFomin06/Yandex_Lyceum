import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
                   UPDATE films
                   SET duration = duration / 3
                   WHERE year = 1973
                   """)
    connect.commit()
    cursor.close()
    connect.close()