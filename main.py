from base.cve_parser import CVEParser
from base.cve_scraper import CVEFetcher
from utils.database import DB


def main():
    # Retrieve the latest CVE entries from the NVD
    fetcher = CVEFetcher(None)
    filename = fetcher.fetch()

    # Filter and retain only the necessary fields before inserting into the database
    parser = CVEParser()
    data = parser.parse(filename)

    # Store and visualize data in the database
    db = DB()
    conn, cursor = db.create_connection()
    #db.view_dbs(cursor)
    db.create_table(cursor)
    db.insert_data(cursor, data)
    #db.view_table(cursor, "cves.cve_database")
    db.stop_connection(conn)


if __name__ == "__main__":
    main()
