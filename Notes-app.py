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

