import sqlite3
from pathlib import Path

DB_NAME = "food_agent.db"

BASE_DIR = Path(__file__).resolve().parents[3]
DB_DIR = BASE_DIR / "DB"
DB_PATH = DB_DIR / DB_NAME

def get_connection():
    print(DB_PATH)
    return sqlite3.connect(DB_PATH)

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            phone_number TEXT PRIMARY KEY,
            category TEXT,
            budget INTEGER,
            diet TEXT,
            style TEXT,
            dish TEXT
            )
        """
        )
    
    conn.commit()

    conn.close()

    print("database created")