import json


class CVEParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            cve_database = {}
            for vuln in data["vulnerabilities"]:
                cve_id = vuln["cve"]["id"]
                cve_database[cve_id] = vuln["cve"]
                cve_database[cve_id]["descriptions"] = vuln["cve"]["descriptions"][0]["value"].replace("\n", "")
                del cve_database[cve_id]["cveTags"]
                if "cvssMetricV40" in vuln["cve"]["metrics"].keys():
                    cve_database[cve_id]["metrics"] = vuln["cve"]["metrics"]["cvssMetricV40"]
                elif "cvssMetricV31" in vuln["cve"]["metrics"].keys():
                    cve_database[cve_id]["metrics"] = vuln["cve"]["metrics"]["cvssMetricV31"]
                elif "cvssMetricV30" in vuln["cve"]["metrics"].keys():
                    cve_database[cve_id]["metrics"] = vuln["cve"]["metrics"]["cvssMetricV30"]
                elif "cvssMetricV2" in vuln["cve"]["metrics"].keys():
                    cve_database[cve_id]["metrics"] = vuln["cve"]["metrics"]["cvssMetricV2"]
                else:
                    print("Il n'y a pas de CVSS : cve-id = "+cve_id)
            with open("cve_db.json", "w", encoding="utf-8") as f:
                json.dump(cve_database, f, ensure_ascii=False, indent=2)
