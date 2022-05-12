import Database
from Database import clear_console
import msvcrt

def main_loop():
        while True:
                clear_console()
                print("Welcome to the notes program!")
                print("1 - Add a note")
                print("2 - View notes")
                print("3 - Exit")
                user_choice = input("Enter your number here: ")
                Database.handle_user_choice(user_choice)

if __name__ == "__main__":
        main_loop()
