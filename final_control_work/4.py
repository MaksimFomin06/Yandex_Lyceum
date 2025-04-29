import sqlite3


def find_genies(magic_ability, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    query = """
    SELECT DISTINCT g.genie
    FROM Genies g
    JOIN Magics m ON g.magic_id = m.id
    JOIN States s ON g.state_id = s.id
    WHERE m.magic = ?
    AND (
        SELECT COUNT(*)
        FROM (
            SELECT lower(substr(s.state, i, 1)) as letter
            FROM (
                WITH RECURSIVE cnt(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM cnt WHERE x < length(s.state))
                SELECT x as i FROM cnt
            )
        )
        WHERE instr(lower(g.genie), letter) > 0
    ) > 0
    ORDER BY length(g.genie), g.genie
    """
    
    cursor.execute(query, (magic_ability,))
    results = cursor.fetchall()
    conn.close()
    
    genies = [result[0] for result in results]
    return genies


def main():
    magic_ability = input().strip()
    db_file = input().strip()

    genies = find_genies(magic_ability, db_file)
    for genie in genies:
        print(genie)


if __name__ == "__main__":
    main()