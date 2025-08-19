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
    def create_table(cursor):
        cursor.execute("CREATE SCHEMA IF NOT EXISTS cves;")
        sql = ''' CREATE TABLE IF NOT EXISTS cves.cve_database(
            cve_id TEXT PRIMARY KEY,
            sourceIdentifier TEXT,
            published DATE,
            lastModified DATE,
            vulnStatus TEXT,
            description TEXT,
            metrics JSONB,
            weaknesses JSONB,
            sources JSONB
        ); '''
        cursor.execute(sql)

    @staticmethod
    def view_table(cursor, table_name):
        cursor.execute("SELECT * FROM "+table_name+" LIMIT 10;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    @staticmethod
    def view_dbs(cursor):
        cursor.execute("SELECT datname FROM pg_database;")
        print(cursor.fetchall())

    @staticmethod
    def stop_connection(conn):
        conn.close()


