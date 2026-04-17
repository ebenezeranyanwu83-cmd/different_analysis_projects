import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute("""
DELETE FROM movies
WHERE title = 'Inception'
""")

conn.commit()
conn.close()