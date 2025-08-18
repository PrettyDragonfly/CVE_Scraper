import json
from datetime import datetime, timedelta
import os
import httpx

class CVEFetcher:
    API_KEY = None
    LAST_RUN_FILE = "last_run.txt"
    BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    CURRENT_DATE = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    def __init__(self, api_key):
        pass

    def read_last_run(self):
        # Last run date initialisation
        if os.path.exists(self.LAST_RUN_FILE):
            with open(self.LAST_RUN_FILE, "r") as f:
                self.LAST_RUN_DATE = f.read().strip()
        else:
            self.LAST_RUN_DATE = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")

        print(f"Dernière récupération : {self.LAST_RUN_DATE}")

    def fetch(self):
        self.read_last_run()
        # Request parameters
        params = {
            "pubStartDate": self.LAST_RUN_DATE,
            "pubEndDate" : self.CURRENT_DATE,
            "resultsPerPage": 2000
        }

        headers = {}
        if self.API_KEY:
            headers["apiKey"] = self.API_KEY

        # Request
        print("Récupération des nouvelles CVE depuis NVD...")
        with httpx.Client() as client:
            response = client.get(self.BASE_URL, params=params)
            try:
                response.raise_for_status()
                data = response.json()
            except:
                print("Request error 404, please check the last run date.")
                exit(1)

        date_str = datetime.utcnow().strftime("%Y_%m_%d")
        filename = f"nvd_new_cve_{date_str}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"{len(data.get('vulnerabilities', []))} nouvelles CVE sauvegardées dans {filename}")

        # Update last update time
        with open(self.LAST_RUN_FILE, "w") as f:
            f.write(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000 UTC"))

        return filename