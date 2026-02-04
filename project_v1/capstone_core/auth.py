# capstone_core/auth.py
# Authentication module for user registration and login
# Handles password hashing and verification using werkzeug security

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from capstone_core.db import get_conn

def register_user(username, password):
    """Register a new user with username and password.
    
    Args:
        username: Unique username (minimum 3 characters)
        password: User password (minimum 6 characters)
    
    Returns:
        Tuple of (success: bool, message: str or user_id)
    """
    # Clean up username input
    username = username.strip()

    # Validate username length
    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    # Validate password length
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    # Hash the password for secure storage (never store plain text passwords)
    password_hash = generate_password_hash(password)

    try:
        # Insert new user into database
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
        return True, "Registration successful."
    except sqlite3.IntegrityError:
        # Username already exists (UNIQUE constraint violation)
        return False, "That username is already taken."

def login_user(username, password):
    """Authenticate a user with username and password.
    
    Args:
        username: Username to authenticate
        password: Password to verify
    
    Returns:
        Tuple of (success: bool, message_or_user_id: str or int)
    """
    # Clean up username input
    username = username.strip()

    # Query database for user credentials
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    # Check if user exists
    if not row:
        return False, "User not found."

    # Extract user data from database result
    user_id, stored_hash = row
    # Verify password against stored hash
    if not check_password_hash(stored_hash, password):
        return False, "Invalid password."

    # Authentication successful - return user ID
    return True, user_id
