from cve_scraper import CVEFetcher
from cve_parser import CVEParser

def main():
    fetcher = CVEFetcher(None)
    filename = fetcher.fetch()

    parser = CVEParser()
    parser.parse(filename)

if __name__ == "__main__":
    main()