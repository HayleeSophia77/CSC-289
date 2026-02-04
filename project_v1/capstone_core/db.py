# capstone_core/db.py
# Database configuration and initialization
# Handles SQLite database connection and table creation

import sqlite3
import os

# Path to SQLite database file (using absolute path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "capstone.db")

def get_conn():
    """Create and return a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection: Database connection object
    """
    return sqlite3.connect(DB_PATH)

def init_db():
    """Initialize the database by creating required tables.
    
    Creates the users table if it doesn't already exist.
    This function is idempotent (safe to run multiple times).
    """
    with get_conn() as conn:
        # Create users table with columns:
        # - id: Unique user identifier (auto-incrementing)
        # - username: Unique username for login
        # - password_hash: Securely hashed password
        # - created_at: Timestamp of account creation
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """)
