import json

class CVEParser:
    def __init__(self):
        pass

    def parse(self, filename):
        # Open and read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            cve_database = {}
            #print(data["vulnerabilities"])
            for vuln in data["vulnerabilities"]:
                print(vuln)
                #print(vuln["cve"]["descriptions"])
                cve_id = vuln["cve"]["id"]
                cve_database[cve_id] = {
                    "published": vuln["cve"]["published"],
                    "last_modified": vuln["cve"]["lastModified"],
                    "vuln_status": vuln["cve"]["vulnStatus"],
                    "description": vuln["cve"]["descriptions"][0]["value"].replace("\n",""),
                    "metrics": vuln["cve"]["metrics"]["cvssMetricV40"]
                }
                with open("cve_db.json", "w", encoding="utf-8") as f:
                    json.dump(cve_database, f, ensure_ascii=False, indent=2)
                print(cve_database)
                break
        # Print the data
        #print(data)