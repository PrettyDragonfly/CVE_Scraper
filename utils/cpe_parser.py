import xml.etree.ElementTree as ET
import json


class CPE:

    FILE_PATH = "../data/official-cpe-dictionary_v2.3.xml"
    def __init__(self):
        pass

    def extract(self, output_file = "../data/patterns.json"):
        tree = ET.parse(self.FILE_PATH)
        root = tree.getroot()

        ns = {
            "cpe": "http://cpe.mitre.org/dictionary/2.0",
            "cpe23": "http://scap.nist.gov/schema/cpe-extension/2.3",
        }

        patterns = []
        seen = set()

        for item in root.findall(".//cpe:cpe-item", ns):
            # --- Version structurée CPE 2.3 ---
            cpe23_item = item.find("cpe23:cpe23-item", ns)
            if cpe23_item is not None:
                name = cpe23_item.attrib.get("name", "")
                parts = name.split(":")  # cpe:2.3:a:vendor:product:version:...

                if len(parts) > 5:
                    vendor = parts[3]
                    product = parts[4]
                    version = parts[5]

                    # Basic clean up
                    product = product.replace("\\", "")
                    vendor = vendor.replace("\\", "")
                    version = version.replace("\\", "")

                    if product and product not in seen and product != "*":
                        seen.add(product)
                        patterns.append({"label": "PRODUCT", "pattern": product})

                    if vendor and vendor not in seen and vendor != "*":
                        seen.add(vendor)
                        patterns.append({"label": "VENDOR", "pattern": vendor})

                    if version and version not in seen and version != "*":
                        seen.add(version)
                        patterns.append({"label": "VERSION", "pattern": version})

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(patterns, f, indent=2, ensure_ascii=False)

        print(f"[✔] {len(patterns)} patterns exportés dans {output_file}")

my_cpe = CPE()
my_cpe.extract()
