import psycopg2

def get_conn():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )

def upsert_repo(name, stars):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO repositories (full_name, stars)
        VALUES (%s, %s)
        ON CONFLICT (full_name)
        DO UPDATE SET stars = EXCLUDED.stars, updated_at = NOW()
    """, (name, stars))

    conn.commit()
    cur.close()
    conn.close()
