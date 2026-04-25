import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")

cursor.execute("""
CREATE TABLE movies (
id INTEGER PRIMARY KEY,
title TEXT,
year INTEGER,
rating REAL
)
""")

movies_list = [
    ("Inception", 2010, 8.8),
    ("Titanic", 1997, 7.9),
    ("The Matrix", 1999, 8.7)
]

cursor.executemany("INSERT INTO movies (title, year, rating) VALUES (?, ?, ?)", movies_list)

conn.commit()
conn.close()