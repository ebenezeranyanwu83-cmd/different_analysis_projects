import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM movies
WHERE year > 1990
ORDER BY rating DESC
""")

for row in cursor.fetchall():
    print(row)

    conn.close()