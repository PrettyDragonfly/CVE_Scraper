import psycopg2


class DB:
    @staticmethod
    def create_connection():
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="dixt-Vafh7",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def create_db(cursor):
        sql = ''' CREATE database cve_database '''
        cursor.execute(sql)
        print("Database cve_database created successfully!")

    @staticmethod
    def view_dbs(cursor):
        cursor.execute("SELECT datname FROM pg_database;")
        print(cursor.fetchall())

    @staticmethod
    def stop_connection(conn):
        conn.close()


