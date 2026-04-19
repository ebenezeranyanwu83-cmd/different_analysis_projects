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
    ("The Matrix", 1999, 8.7),
    ("Ocean's Eleven", 2001, 7.7),
    ("Gladiator" , 2000, 8.5),
    ("Toy Story 2", 1999, 7.9),
    ("Blade", 1998, 7.1),
    ("Face/Off", 1997, 7.3),
    ("Men In Black", 1997, 7.3),
    ("Rush Hour", 1998, 7.0),
    ("X-Men", 2000, 7.3),
    ("Shrek", 2001, 7.9)

]

cursor.executemany("INSERT INTO movies (title, year, rating) VALUES (?, ?, ?)", movies_list)

conn.commit()
conn.close()