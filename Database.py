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

def update_note(updated_text: str, note_id: str):
    conn = sqlite3.connect('notes.sql')
    curs = conn.cursor()

    curs.execute(f"""
            UPDATE notes
            SET text = '{updated_text}'
            WHERE rowid = {note_id}
    """)
    conn.commit()
    conn.close()

def search_note_by_id(note_id: str) -> list:
    conn = sqlite3.connect('notes.sql')
    curs = conn.cursor()

    curs.execute(f"""
            SELECT rowid, *
            FROM notes
            WHERE rowid = {int(note_id)}
    """)
    note = curs.fetchall()
    conn.close()
    return note

def delete_note(note_id: str):
    conn = sqlite3.connect("notes.sql")
    curs = conn.cursor()

    curs.execute(f"""
            DELETE FROM notes
            WHERE rowid = {note_id} 
    """)
    conn.commit()
    conn.close()

def press_any_key():
    print("\nPress any key...")
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

def user_choice_update_note():
    clear_console()
    note_id = input("Enter the id of the note you want to change: ")
    try:
        int(note_id)
    except:
        print("Error. You should enter a number, not a text!")
        print("Try again.")
        press_any_key()
        return
    try:
        old_note = search_note_by_id(note_id)
    except:
        print("Wrong id, or some other error... Try again.")
        press_any_key()
        return
    if not old_note:
        print("There is no such note! Try again.")
        press_any_key()
        return
    print(f"Old text: {old_note[0][2]}")
    updated_text = input("Enter updated text here: ")
    try:
        update_note(updated_text, note_id)
        print("Success! Not has been updated.")
        press_any_key()
        return
    except:
        print("Error... Try again later")
        press_any_key()
        return

def user_choice_delete_note():
    clear_console()
    note_id = input("Enter the id of the note you want to delete: ")
    try:
        int(note_id)
    except:
        print("Error. You should enter a number, not a text!")
        print("Try again.")
        press_any_key()
        return
    try:
        old_note = search_note_by_id(note_id)
    except:
        print("Wrong id, or some other error... Try again.")
        press_any_key()
        return
    if not old_note:
        print("There is no such note! Try again.")
        press_any_key()
        return
    print("Deleting your note...")
    try:
        delete_note(note_id)
    except:
        print("Error, something went wrong... Try again.")
        press_any_key()
        return
    print("Success! Your note has been removed.")
    press_any_key()

def handle_user_choice(user_choice: str):
    valid_choices = ['1', '2', '3', '4', '5']
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
        user_choice_update_note()
    elif user_choice == '4':
        user_choice_delete_note()
    elif user_choice == '5':
        user_choice_exit_program()