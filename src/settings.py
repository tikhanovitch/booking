import os

from dotenv import load_dotenv

load_dotenv(".env")

DB_PORT = os.environ.get("DB_PORT")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

SYNC_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
ASYNC_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SECRET = os.environ.get("SECRET")
COOKIE_MAX_AGE = os.environ.get("COOKIE_MAX_AGE")
LIFETIME_SECONDS = os.environ.get("LIFETIME_SECONDS")
JWT_NAME = os.environ.get("JWT_NAME")

ECHO = True
AUTOCOMMIT = False
AUTOFLUSH = False
