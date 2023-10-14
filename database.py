import psycopg2
from config import Config

conn = psycopg2.connect(
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    dbname=Config.DB_NAME,
    password=Config.DB_PASSWORD,
    user=Config.DB_USER,
)
cur = conn.cursor()
