# capstone_core/functions.py
from capstone_core.auth import register_user, login_user

def main_menu() -> int:
    print("\n==== Main Menu ====")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter choice: ").strip()
    if not choice.isdigit():
        return 0
    return int(choice)

def user_registration():
    print("\n--- New User Registration ---")
    username = input("Username: ")
    password = input("Password: ")
    full_name = input("Full name (optional): ")
    company_name = input("Company name (optional): ")

    ok, msg = register_user(username, password, full_name, company_name)
    print(msg)

def user_login():
    print("\n--- User Login ---")
    username = input("Username: ")
    password = input("Password: ")

    ok, result = login_user(username, password)
    if ok:
        print(f"Login successful! (User ID: {result})")
    else:
        print(result)
