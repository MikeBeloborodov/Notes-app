import os
import sqlite3
import datetime
import msvcrt

def create_database() -> bool:
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
        return True
    else: return False

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
            SELECT rowid, *
            FROM notes
    """)
    notes = curs.fetchall()
    conn.close()

    return notes

def press_any_key():
    print("Press any key...")
    msvcrt.getch()

def clear_console():
    os.system('CLS')

def user_choice_view_notes():
        clear_console()
        # returns true if database didn't exist before
        if create_database():
            print("I've just created a new database for you!")
            print("It's empty now, let's add a note!")
            press_any_key()
            return
            
        notes = retrieve_all_notes()
        if not notes:
            print("Database is empty :(")
            print("Please add some notes!")
            press_any_key()
            return

        clear_console()
        for note in notes:
            print("---------------------------")
            print(f"Note id: {note[0]}")
            print(f"Date added: {note[1]}")
            print(f"Text: {note[2]}")
        press_any_key()
        return

def user_choice_add_new_note():
        clear_console()
        # returns true if database didn't exist before
        if create_database():
            print("I just created a new database for you!")
            print("It's empty now, let's add a note!")

        print("What should I save in a note?")
        new_note_text = input("Your text here: ")
        try:
            add_note_to_db(new_note_text)
            print("Note added succesfully!")
            press_any_key()
        except:
            print("Something went wrong... Please try again.")
            press_any_key()
            return

def user_choice_exit_program():
        clear_console()
        print("Goodbye!")
        press_any_key()
        exit()

def handle_user_choice(user_choice: str):
    valid_choices = ['1', '2', '3']
    if user_choice not in valid_choices:
        print("Error. Please try again.")
        print("Press any key...")
        press_any_key()
        return
    elif user_choice == '1':
        user_choice_add_new_note()
    elif user_choice == '2':
        user_choice_view_notes()
    elif user_choice == '3':
        user_choice_exit_program()