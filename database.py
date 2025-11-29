import sqlite3
from datetime import datetime


def init_bd():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT,
            register_at TEXT
        )
        """)



def add_user(user_id, username):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        register_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT OR IGNORE INTO users(id, username, register_at) 
        VALUES(?, ?, ?)
        """, (user_id, username, register_at))
        t=cursor.execute("""
        SELECT * FROM users
        """)
        print(*t)


        conn.commit()


















