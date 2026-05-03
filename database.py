import sqlite3

def connect():
    return sqlite3.connect("health.db", check_same_thread=False)

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS health(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        weight REAL,
        calories INTEGER,
        steps INTEGER,
        water INTEGER
    )
    """)

    conn.commit()
    conn.close()

def add_entry(date, weight, calories, steps, water):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO health (date, weight, calories, steps, water) VALUES (?, ?, ?, ?, ?)",
        (date, weight, calories, steps, water)
    )

    conn.commit()
    conn.close()

def get_entries():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM health")
    rows = cur.fetchall()

    conn.close()
    return rows

def delete_entry(entry_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM health WHERE id=?", (entry_id,))

    conn.commit()
    conn.close()