import os
import sqlite3
import datetime

def make_database():
    if not os.path.exists("notes.sql"):
        conn = sqlite3.connect("notes.sql")
        curs = conn.cursor()

        curs.execute("""
                CREATE TABLE notes (
                    date_created TEXT,
                    text TEXT,
                    date_updated TEXT
                )
        """)

        conn.commit()
        conn.close()

def add_note_to_db(text: str):
    conn = sqlite3.connect("notes.sql")
    curs = conn.cursor()

    date = str(datetime.datetime.now())[:10]

    curs.execute(f"""
                INSERT INTO notes
                VALUES ('{date}', '{text}', '{date}')
    """)

    conn.commit()
    conn.close()

def retrieve_all_notes() -> list:
    conn = sqlite3.connect("notes.sql")
    curs = conn.cursor()

    curs.execute("""
            SELECT *
            FROM notes
    """)
    notes = curs.fetchall()
    conn.close()

    return notes