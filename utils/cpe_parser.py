import json
import glob
import os


class CPE:

    FILE_PATH_BRUT = "../data/nvdcpe/*.json"
    FILE_PATH_PRETTY = "../data/nvdcpe_pretty/"

    def __init__(self):
        pass

    def reformat(self):

        # Création du dossier de sortie
        os.makedirs(self.FILE_PATH_PRETTY, exist_ok=True)

        for file_path in glob.glob(self.FILE_PATH_BRUT):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            new_file_path = file_path.replace("../data/nvdcpe/", "").replace(".json","")

            with open(self.FILE_PATH_PRETTY+new_file_path+"_pretty.json", "w",
                   encoding="utf-8") as f:
                 json.dump(data, f, indent=4, ensure_ascii=False)

    # Convert cpe database to NLP Model
    def build_model(self):

        products = []

        # Parcours de tous les fichiers JSON de la base
        for file_path in glob.glob(self.FILE_PATH_PRETTY+"*.json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(data.keys())

                for item in data.get("products", []):
                    cpe_info = item.get("cpe", {})
                    cpe_name = cpe_info.get("cpeName")
                    title_entries = cpe_info.get("titles", [])
                    title = next((t["title"] for t in title_entries if t["lang"] == "en"), "")
                    products.append({"cpe_name": cpe_name, "title": title})
                print(products)
