import spacy
from utils.cpe_parser import CPE
import os

class NLP:

    nlp = spacy.blank("en")
    my_cpe = CPE()
    MODEL_PATH = "data/nlp_model_with_cpe_patterns"

    def __init__(self):
        pass

    def create_model(self):
        # If model exists
        if os.path.exists(self.MODEL_PATH):
            print(f"Modèle existant trouvé, chargement depuis {self.MODEL_PATH}")
            self.nlp = spacy.load(self.MODEL_PATH)
            return

        ruler = self.nlp.add_pipe("entity_ruler")

        # Load products
        products = self.my_cpe.build_model()

        patterns = [{"label": "PRODUCT", "pattern": p["title"]} for p in products if p["title"]]
        ruler.add_patterns(patterns)

        print(f"✅ {len(patterns)} patterns ajoutés")

        # Save model
        self.nlp.to_disk(self.MODEL_PATH)

    def analyze(self, text):
        doc = self.nlp(text)
        print([(ent.label_, ent.text) for ent in doc.ents])