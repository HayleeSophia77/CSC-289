# capstone_core/auth.py
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from capstone_core.db import get_conn

def register_user(username, password, full_name="", company_name=""):
    username = username.strip()

    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    password_hash = generate_password_hash(password)

    try:
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash, full_name, company_name) VALUES (?, ?, ?, ?)",
                (username, password_hash, full_name.strip() or None, company_name.strip() or None)
            )
        return True, "Registration successful."
    except sqlite3.IntegrityError:
        return False, "That username is already taken."

def login_user(username, password):
    username = username.strip()

    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if not row:
        return False, "User not found."

    user_id, stored_hash = row
    if not check_password_hash(stored_hash, password):
        return False, "Invalid password."

    return True, user_id
