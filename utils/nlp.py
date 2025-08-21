import json
import spacy
from spacy.matcher import Matcher

# Chargement du modèle
nlp = spacy.blank("en")
#nlp = spacy.load("../data/patterns.json")

# Créer le matcher
matcher = Matcher(nlp.vocab)