from Database import clear_console, handle_user_choice

def main():
        while True:
                clear_console()
                print("Welcome to the notes program!")
                print("1 - Add note")
                print("2 - View notes")
                print("3 - Update note")
                print("4 - Delete note")
                print("5 - Search notes by keyword")
                print("6 - Exit")
                user_choice = input("Enter your number here: ")
                handle_user_choice(user_choice)

if __name__ == "__main__":
        main()
