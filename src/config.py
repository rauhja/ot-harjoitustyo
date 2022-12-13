import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

USERS_FILENAME = os.getenv("USERS_FILENAME") or "users.db"
USERS_FILE_PATH = os.path.join(dirname, "..", USERS_FILENAME)

SCORE_FILENAME = os.getenv("SCORE_FILENAME") or "score.db"
SCORE_FILE_PATH = os.path.join(dirname, "..", SCORE_FILENAME)
