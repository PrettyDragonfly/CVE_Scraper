import psycopg2
import json


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
            cvss NUMERIC,
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
        print("Table cves.cve_database created successfully!")

    @staticmethod
    def insert_data(cursor, data):
        sql = """
            INSERT INTO cves.cve_database (
                cve_id, cvss, sourceIdentifier, published, lastModified, vulnStatus,
                description, metrics, weaknesses, sources
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (cve_id) DO NOTHING;
        """
        for vuln in data:
            # Fix des exceptions
            if data[vuln]["metrics"]:
                cvss = data[vuln]["metrics"][0]["cvssData"]["baseScore"]
            else:
                cvss = None
            if data[vuln]["weaknesses"]:
                weaknesses = data[vuln]["weaknesses"][0]
            else:
                weaknesses = None
            cursor.execute(sql, (
                data[vuln]["id"],
                cvss,
                data[vuln]["sourceIdentifier"],
                data[vuln]["published"],
                data[vuln]["lastModified"],
                data[vuln]["vulnStatus"],
                data[vuln]["descriptions"],
                json.dumps(data[vuln]["metrics"]),  # dict → JSON
                json.dumps(weaknesses),  # dict/list → JSON
                json.dumps(data[vuln]["sources"])  # dict/list → JSON
            ))

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


