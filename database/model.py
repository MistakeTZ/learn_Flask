import psycopg2
from psycopg2.extensions import connection, cursor
from psycopg2.extras import RealDictCursor
from os import getenv

conn: connection
cur: cursor
dict_cur: cursor


class DB():
    
    def load_database(dbname = "", user = "", password = "", host = "", port=0):
        global conn, cur, dict_cur

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
        dict_cur = conn.cursor(cursor_factory=RealDictCursor)

        try:
            cur.execute("SELECT version()")
            print(" ".join(cur.fetchone()[0].split()[:2]), "connected")
        except:
            raise ValueError("Connection to database failed")


    def create_tables():
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                         id serial PRIMARY KEY,
                         name VARCHAR(255),
                         value BOOL DEFAULT false
                         )""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS restaurants (
                         restaurant_id serial PRIMARY KEY,
                         name VARCHAR(255),
                         address VARCHAR(255),
                         stars DECIMAL(3, 2) DEFAULT 0,
                         description TEXT
                         )""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS dishes (
                         dish_id serial PRIMARY KEY,
                         restaurant_id INT NOT NULL REFERENCES restaurants,
                         name VARCHAR(255),
                         price FLOAT NOT NULL,
                         available BOOL DEFAULT true,
                         description TEXT
                         )""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                         dish_id serial PRIMARY KEY,
                         restaurant_id INT NOT NULL REFERENCES restaurants,
                         name VARCHAR(255),
                         price FLOAT NOT NULL,
                         available BOOL DEFAULT true,
                         description TEXT
                         )""")
        conn.commit()


    def select(by_value, field="id", table="users"):
        return DB.get("SELECT * FROM {} WHERE {} = %s".format(table, field), [by_value], True)
    

    def get(prompt, values=None, one=False):
        try:
            cur.execute(prompt, values)
            if one:
                return cur.fetchone()
            else:
                return cur.fetchall()
        except Exception as e:
            print(e)
            return False
        

    def get_dict(prompt, values=None, one=False):
        try:
            dict_cur.execute(prompt, values)
            if one:
                return dict(dict_cur.fetchone())
            else:
                return [dict(res) for res in dict_cur.fetchall()]
        except Exception as e:
            print(e)
            return False
        

    def commit(prompt, values=None):
        try:
            cur.execute(prompt, values)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def unload_database():
        conn.close()

