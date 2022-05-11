import sqlite3
import datetime

def make_database():
        # connects to a database file or creates it
        connection = sqlite3.connect('notes.db')
        # create a cursor
        curs = connection.cursor()
        # create a table
        curs.execute("""CREATE TABLE notes (
                        note_date text,
                        note_text text,
                        note_last_update text
                )""")
        # NULL, INTEGER, REAL, TEXT, BLOB (could be a pic, mp3... any file as is)
        # commit our execute
        connection.commit()
        # close the connection
        connection.close()

def insert_data_to_database(note_text: str):
        connection = sqlite3.connect('notes.db')
        print("Connected to database...")
        curs = connection.cursor()
        date = str(datetime.datetime.now())[:10]
        curs.execute(f"INSERT INTO notes VALUES ('{date}', '{note_text}', '{date}')")
        connection.commit()
        print("Inserted new data...")
        print("Connection closed!")

def insert_many_data(notes: list[str]):
        connection = sqlite3.connect('notes.db')
        print("Connected to database...")
        curs = connection.cursor()
        date = str(datetime.datetime.now())[:10]

        notes_tuples = [(date, text, date) for text in notes]

        # execute and executemany are different
        # 3 question marks means that we add only 3 tuples
        curs.executemany(f"INSERT INTO notes VALUES (?,?,?)", notes_tuples)
        
        connection.commit()
        print("Inserted a lot of data...")
        print("Connection closed!")

def fetch_data_from_db() -> list:
        connection = sqlite3.connect('notes.db')
        curs = connection.cursor()
        curs.execute("SELECT * FROM notes")
        
        # curs.fetchall()
        # curs.fetchmany()
        # curs.fetchone()

        # returns a list with every note
        data = curs.fetchall()
        
        connection.commit()
        connection.close()

        return data

def get_unique_id() -> list:
        connection = sqlite3.connect("notes.db")
        curs = connection.cursor()

        # rowid is a unique id that sqlite gives to an entry (1, 2, 3 ...)
        curs.execute("SELECT rowid, * FROM notes")

        data = curs.fetchall()

        return data

def search_data_base():
        conn = sqlite3.connect("notes.db")
        curs = conn.cursor()

        # WHERE is a keyword for searching
        # LIKE is a keyword for uncertain value
        # % sign cuts this search word and searches in any strings
        curs.execute("SELECT * FROM notes WHERE note_text LIKE '%First%'")
        
        searched_data = curs.fetchall()

        return searched_data

def update_data_base(new_text: str):
        conn = sqlite3.connect("notes.db")
        curs = conn.cursor()

        date = str(datetime.datetime.now())[:10]
        # you can update with keywords UPDATE tablename SET new value
        # don't forget ' ' !!!!
        # you can also use rowid to pinpoint certain 
        curs.execute(f"""
                UPDATE notes
                SET note_text = '{new_text}',     
                note_last_update = '{date}'
                WHERE note_text LIKE '%First%'        
        """)
        print("Succesfully updated data base!")
        conn.commit()
        conn.close()

def delete_from_data_base():
        conn = sqlite3.connect("notes.db")
        curs = conn.cursor()

        # don't forget % % from both sides, if this if not the beginning
        # or the end of the text
        curs.execute("""
                DELETE from notes WHERE note_text LIKE '%3d%'
        """)

        print("Deleted from db!")
        conn.commit()
        conn.close()

def order_data_base() -> list:
        conn = sqlite3.connect("notes.db")
        curs = conn.cursor()

        # ASC - ascending, DESC - descending
        curs.execute("""
        SELECT rowid, *
        FROM notes
        ORDER BY rowid DESC""")

        data = curs.fetchall()

        conn.commit()
        conn.close()

        return data



