import sqlite3
from config import SCORE_FILE_PATH

connection = sqlite3.connect(SCORE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_score_db_connection():
    return connection
