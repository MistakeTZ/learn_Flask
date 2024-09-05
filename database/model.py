import psycopg2
from psycopg2.extensions import connection, cursor
from os import getenv

conn: connection
cur: cursor


class DB():
    
    def load_database(dbname = "", user = "", password = "", host = "", port=0):
        global conn, cur

        if not dbname:
            dbname = getenv("dbname")
        if not user:
            user = getenv("dbuser")
        if not password:
            password = getenv("dbpassword")
        if not host:
            host = getenv("dbhost")
        if not port:
            port = getenv("dbport")

        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        try:
            cur.execute("SELECT version()")
            print(cur.fetchone()[0])
        except:
            raise ValueError("Connection to database failed")


    def create_table():
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                         id INT PRIMARY KEY,
                         name VARCHAR(255),
                         value BOOL DEFAULT false
                         )""")
        conn.commit()


    def select(by_value, field="id", table="users"):
        cur.execute("SELECT * FROM {} WHERE {} = %s".format(table, field), [by_value])
        return cur.fetchone()


    def unload_database():
        conn.close()

