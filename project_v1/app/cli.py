# Main CLI application entry point
# This module handles the command-line interface for user authentication

import capstone_core.functions as fn
from capstone_core.db import init_db

def main():
    """Main application loop that displays menu and handles user choices."""
    # Initialize database and create tables if they don't exist
    init_db()

    # Main application loop - runs until user chooses to exit
    while True:
        # Display menu and get user's choice
        value = fn.main_menu()

        # Handle user login
        if value == 1:
            fn.user_login()
        # Handle new user registration
        elif value == 2:
            fn.user_registration()
        # Exit the application
        elif value == 3:
            print("Exiting...")
            break
        # Invalid input handling
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
