
import sqlite3
from pathlib import Path
from contextlib import contextmanager
from math import isfinite


# =========================================================
# CONFIGURATION
# =========================================================

DATABASE = Path(__file__).resolve().parent / "memory.db"


# =========================================================
# DATABASE CONNECTION MANAGEMENT
# =========================================================

def get_connection():

    connection = sqlite3.connect(
        str(DATABASE),
        timeout=10
    )

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


@contextmanager
def database_connection():

    connection = get_connection()

    try:
        yield connection
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


# =========================================================
# DATABASE INITIALIZATION
# =========================================================

def init_db():

    with database_connection() as connection:

        cursor = connection.cursor()

        # Memories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                importance REAL DEFAULT 1.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Chat history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                deleted INTEGER NOT NULL DEFAULT 0
            )
        """)

        # Check existing columns
        cursor.execute("PRAGMA table_info(chat_history)")

        columns = {
            column[1]
            for column in cursor.fetchall()
        }

        # Migration: deleted column
        if "deleted" not in columns:

            cursor.execute("""
                ALTER TABLE chat_history
                ADD COLUMN deleted INTEGER NOT NULL DEFAULT 0
            """)

        # Indexes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_memories_importance
            ON memories (importance DESC, created_at DESC)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chat_history_deleted
            ON chat_history (deleted, id DESC)
        """)


# =========================================================
# MEMORY OPERATIONS
# =========================================================

def save_memory(content, importance=1.0):

    if not isinstance(content, str) or not content.strip():
        raise ValueError("Memory content cannot be empty.")

    if (
        isinstance(importance, bool)
        or not isinstance(importance, (int, float))
        or not isfinite(importance)
    ):
        raise ValueError("Importance must be a finite number.")

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO memories (content, importance)
            VALUES (?, ?)
        """, (
            content.strip(),
            importance
        ))

        return cursor.lastrowid


def get_memories():

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, content, importance, created_at
            FROM memories
            ORDER BY importance DESC, created_at DESC
        """)

        return cursor.fetchall()


# =========================================================
# CHAT HISTORY OPERATIONS
# =========================================================

def save_chat(user_message, ai_response):

    if not isinstance(user_message, str) or not user_message.strip():
        raise ValueError("User message cannot be empty.")

    if not isinstance(ai_response, str):
        raise ValueError("AI response must be a string.")

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO chat_history (
                user_message,
                ai_response
            )
            VALUES (?, ?)
        """, (
            user_message,
            ai_response
        ))

        return cursor.lastrowid


def update_chat(chat_id, user_message, ai_response):

    if not isinstance(user_message, str) or not user_message.strip():
        raise ValueError("User message cannot be empty.")

    if not isinstance(ai_response, str):
        raise ValueError("AI response must be a string.")

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE chat_history
            SET
                user_message = ?,
                ai_response = ?
            WHERE id = ? AND deleted = 0
        """, (
            user_message,
            ai_response,
            chat_id
        ))

        return cursor.rowcount > 0


def get_chat_history(limit=20):

    if (
        isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 1
    ):
        raise ValueError("Limit must be a positive integer.")

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, user_message, ai_response, created_at
            FROM chat_history
            WHERE deleted = 0
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        return cursor.fetchall()


def get_chat(chat_id):

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, user_message, ai_response, created_at
            FROM chat_history
            WHERE id = ? AND deleted = 0
        """, (chat_id,))

        return cursor.fetchone()


# =========================================================
# CHAT DELETION
# =========================================================

def delete_chat(chat_id):

    with database_connection() as connection:

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE chat_history
            SET deleted = 1
            WHERE id = ? AND deleted = 0
        """, (chat_id,))

        return cursor.rowcount > 0


# =========================================================
# BACKWARD COMPATIBILITY
# =========================================================

def add_deleted_column():

    init_db()


# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

if __name__ == "__main__":

    init_db()

    print("Database initialized successfully.")
    print(f"Database location: {DATABASE}")
