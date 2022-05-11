import sqlite3

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
