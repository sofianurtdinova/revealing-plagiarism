import sqlite3

DB_FILE = 'plagiarism.db'
DATABASE_URL = f'sqlite:///{DB_FILE}'


def get_connection():
    """
    Return the connection with DB.
    """
    conn = sqlite3.connect(DB_FILE)
    return conn
