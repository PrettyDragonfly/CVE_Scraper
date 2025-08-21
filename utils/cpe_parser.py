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

