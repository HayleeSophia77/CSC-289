# capstone_core/functions.py
# UI/Menu functions for command-line interface
# Handles user input and displays menus for authentication workflows

from capstone_core.auth import register_user, login_user

def main_menu() -> int:
    """Display the main menu and get user's choice.
    
    Returns:
        int: User's menu choice (1-3), or 0 if invalid input
    """
    # Display menu options
    print("\n==== Main Menu ====")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    # Get and validate user input
    choice = input("Enter choice: ").strip()
    if not choice.isdigit():
        return 0  # Invalid input - return 0
    return int(choice)

def user_registration():
    """Handle the user registration workflow.
    
    Prompts for username, password, and optional profile information,
    then calls the register_user function to create the account.
    """
    print("\n--- New User Registration ---")
    # Collect user information
    username = input("Username: ")
    password = input("Password: ")
    

    # Attempt to register the user
    ok, msg = register_user(username, password)
    # Display result message (success or error)
    print(msg)

def user_login():
    """Handle the user login workflow.
    
    Prompts for username and password, then attempts authentication.
    Displays success message with user ID or error message.
    """
    print("\n--- User Login ---")
    # Collect credentials
    username = input("Username: ")
    password = input("Password: ")

    # Attempt to authenticate user
    ok, result = login_user(username, password)
    if ok:
        # Login successful - result contains user ID
        print(f"Login successful! (User ID: {result})")
    else:
        # Login failed - result contains error message
        print(result)
