import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute("""
SELECT title, rating
FROM movies
ORDER BY rating DESC
LIMIT 5
""")

print("Top 5 movies:")
for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT AVG(rating) FROM movies")

print("\nAverage rating:")
print(cursor.fetchone())

cursor.execute("""
SELECT title, year
FROM movies
WHERE year > 2000
""")

print("\nMovies after 2000:")
for row in cursor.fetchall():
    print(row)

    conn.close()