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

        try:
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        except Exception as e:
            raise ValueError("Cannot connect to database.\nException:\n{}".format(e))
        cur = conn.cursor()

        try:
            cur.execute("SELECT version()")
            print(" ".join(cur.fetchone()[0].split()[:2]), "connected")
        except:
            raise ValueError("Connection to database failed")


    def create_table():
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                         id serial PRIMARY KEY,
                         name VARCHAR(255),
                         value BOOL DEFAULT false
                         )""")
        conn.commit()


    def select(by_value, field="id", table="users"):
        return DB.get("SELECT * FROM {} WHERE {} = %s".format(table, field), [by_value], True)
    

    def get(prompt, values=None, one=False):
        cur.execute(prompt, values)
        if one:
            return cur.fetchone()
        else:
            return cur.fetchall()
        

    def commit(prompt, values=None):
        cur.execute(prompt, values)
        conn.commit()


    def unload_database():
        conn.close()

