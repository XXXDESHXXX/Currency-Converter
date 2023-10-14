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


def create_tables():
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS auth_user
        (
            id serial NOT NULL,
            username character varying(48) NOT NULL,
            password character varying(256) NOT NULL,
            PRIMARY KEY (id)
        );
        
        CREATE TABLE IF NOT EXISTS convertation_history
        (
            id serial NOT NULL,
            from_currency character varying(16) NOT NULL,
            to_currency character varying(16) NOT NULL,
            amount numeric NOT NULL,
            created_at timestamp with time zone NOT NULL,
            user_id serial REFERENCES auth_user(id) NOT NULL,
            PRIMARY KEY (id)
        );
        """
    )
    conn.commit()
