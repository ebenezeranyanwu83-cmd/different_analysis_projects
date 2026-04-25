import sqlite3
from sqlite3 import Connection

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute("""
UPDATE movies
SET rating = 9.0
WHERE title = 'The Matrix'
""")

conn.commit()
conn.close()