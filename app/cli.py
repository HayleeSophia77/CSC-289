
import capstone_core.functions as fn
from capstone_core.db import init_db

def main():
    init_db()  # run once on startup

    while True:
        value = fn.main_menu()

        if value == 1:
            fn.user_login()
        elif value == 2:
            fn.user_registration()
        elif value == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
