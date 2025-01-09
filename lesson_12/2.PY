import sqlite3


def get_result(name) -> None:
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE films
        SET duration = '42'
        WHERE duration = ''
    """)
    connect.commit()
    cursor.close()
    connect.close()