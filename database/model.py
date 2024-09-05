import psycopg2
from psycopg2.extensions import connection
from os import getenv


class DB():
    conn: connection

    def load_database(self, dbname = "", user = "", password = "", host = "", port=0):
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

        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

