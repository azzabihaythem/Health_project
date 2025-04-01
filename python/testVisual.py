import unittest
import pandas as pd
from pymongo import MongoClient



class TestMongoDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    
        """Configuration de la connexion à MongoDB et chargement du fichier CSV."""
        #csv_file_path = "/data/csv/healthcare_dataset.csv"
        csv_file_path = "/data/csv/healthcare_dataset_nettoye.csv"
        cls.df = pd.read_csv(csv_file_path, delimiter=";")
        cls.client = MongoClient("mongodb://admin:admin#75*Db@mongo:27017/")
        cls.db = cls.client["medical_db"]
        cls.collection = cls.db["patients"]


    def test_duplicate_insertion(self):
        """Vérifie si le nombre de lignes est identique entre Pandas et MongoDB."""
        nb_lignes_pandas = len(self.df)
        nb_lignes_mongo = self.collection.count_documents({})  # Utiliser la collection de test

        print(f"Lignes dans Pandas : {nb_lignes_pandas}")
        print(f"Lignes dans MongoDB : {nb_lignes_mongo}")

        self.assertEqual(nb_lignes_pandas, nb_lignes_mongo)  # Comparer les nombres et non des ensembles


    def test_column_count(self):
        """Vérifie si le nombre de colonnes est identique entre Pandas et MongoDB."""

        nb_colonnes_pandas = len(self.df.columns)
    # Récupérer un document de MongoDB et compter ses clés
        un_document = self.collection.find_one({})
        nb_colonnes_mongo = len(un_document.keys()) if un_document else 0

        print(f"Colonnes dans Pandas : {nb_colonnes_pandas}")
        print(f"Colonnes dans MongoDB : {nb_colonnes_mongo}")

        #self.assertIn("_id", un_document, "La colonne '_id' est absente de MongoDB mais attendue.")
        self.assertEqual(nb_colonnes_pandas+1, nb_colonnes_mongo)


if __name__ == "__main__":
    unittest.main()