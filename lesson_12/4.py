import sqlite3


def get_result(name):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
                   DELETE FROM films 
                   WHERE title LIKE 'Я%а'
                   """)
    connect.commit()
    cursor.close()
    connect.close()