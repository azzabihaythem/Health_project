import unittest
import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv


class TestMongoDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    
        """Configuration de la connexion à MongoDB et chargement du fichier CSV."""
        load_dotenv()
        csv_file_path = "/data/csv/healthcare_dataset_nettoye.csv"
        #csv_file_path = "C:/Users/zanno/Desktop/Formation_Data_engineer/Projet4/archive/healthcare_dataset_nettoye.csv"
        cls.df = pd.read_csv(csv_file_path, delimiter=";")
        #cls.client = MongoClient("mongodb://admin:******@mongo:27017/")
        # Récupérer les variables d'environnement
        admin_username = os.getenv("MONGO_ADMIN_USERNAME")
        admin_password = os.getenv("MONGO_ADMIN_PASSWORD")
        mongo_host = os.getenv("MONGO_HOST")
        mongo_port = os.getenv("MONGO_PORT")
        client =  MongoClient(f"mongodb://{admin_username}:{admin_password}@{mongo_host}:{mongo_port}/")


       # cls.client = MongoClient("mongodb://localhost:27017/")
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


    def test_Gender_count(self):
        """Vérifie si le nombre de patients male et femelle est identique entre Pandas et MongoDB."""
        patients_homme_pandas = len(self.df[self.df["Gender"].str.lower() == "male"])
        patients_femme_pandas = len(self.df[self.df["Gender"].str.lower() == "female"])
        patients_homme_mongo = self.collection.count_documents({"Gender":"Male"})  # Utiliser la collection de test
        patients_femme_mongo = self.collection.count_documents({"Gender":"Female"}) 

        print(f"Lignes dans Pandas male :{patients_homme_pandas}")
        print(f"Lignes dans Mongo male : {patients_homme_mongo}")
        self.assertEqual(patients_homme_pandas, patients_homme_mongo) 
 
        print(f"Lignes dans Panda femelle: {patients_femme_pandas}")
        print(f"Lignes dans Mongo femelle: {patients_femme_mongo}")
        self.assertEqual(patients_femme_mongo ,patients_femme_pandas)  



if __name__ == "__main__":
    unittest.main()