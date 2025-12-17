import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
    INSERT INTO repositories (full_name, stars)
    VALUES ('test/repo', 123)
    ON CONFLICT (full_name)
    DO UPDATE SET stars = EXCLUDED.stars
""")

conn.commit()

cur.execute("SELECT * FROM repositories;")
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()
