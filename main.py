from cve_scraper import CVEFetcher
from cve_parser import CVEParser
from database import DB


def main():
    # Fetching des données sur NVD
    fetcher = CVEFetcher(None)
    filename = fetcher.fetch()

    # Parsing des données pour garder que ce qui nous intéresse
    parser = CVEParser()
    data = parser.parse(filename)

    # Stockage et visualisation des données dans la DB
    db = DB()
    conn, cursor = db.create_connection()
    #db.view_dbs(cursor)
    db.create_table(cursor)
    db.insert_data(cursor, data)
    #db.view_table(cursor, "cves.cve_database")
    db.stop_connection(conn)


if __name__ == "__main__":
    main()
