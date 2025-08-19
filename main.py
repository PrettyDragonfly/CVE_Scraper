from cve_scraper import CVEFetcher
from cve_parser import CVEParser
from database import DB


def main():
    fetcher = CVEFetcher(None)
    filename = fetcher.fetch()

    parser = CVEParser()
    parser.parse(filename)

    db = DB()
    conn, cursor = db.create_connection()
    db.view_dbs(cursor)
    db.create_table(cursor)
    db.view_table(cursor, "cves.cve_database")
    db.stop_connection(conn)


if __name__ == "__main__":
    main()
