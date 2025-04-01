import pandas as pd
from pymongo import MongoClient

# Connexion à MongoDB
#client = MongoClient('mongodb://localhost:27017/')
client =  MongoClient("mongodb://admin:admin#75*Db@mongo:27017/")
db = client['medical_db']  # Nom de la base
collection = db['patients']  # Nom de la collection

# Charger le fichier CSV
csv_file_path = "/data/csv/healthcare_dataset_nettoye.csv"


df = pd.read_csv(csv_file_path,delimiter=";")



df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["Billing Amount"] = pd.to_numeric(df["Billing Amount"],errors='coerce')
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"],dayfirst=True)  # Convertir en datetime
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"],dayfirst=True)  # Convertir en datetime

#  Convertir datetime64 en format compatible MongoDB
df["Date of Admission"] = df["Date of Admission"].apply(lambda x: x.to_pydatetime() if pd.notnull(x) else None)
df["Discharge Date"] = df["Discharge Date"].apply(lambda x: x.to_pydatetime() if pd.notnull(x) else None)


# Convertir le DataFrame en liste de dictionnaires
data_dict = df.to_dict(orient="records")

#  Insérer dans MongoDB
collection.insert_many(data_dict)

print("Données insérées avec succès !")

# Vérifier le nombre de lignes insérées après insertion
nb_lignes_pandas = len(df)
nb_lignes_mongo = collection.count_documents({})

print(f"Lignes dans Pandas : {nb_lignes_pandas}")
print(f"Lignes dans MongoDB : {nb_lignes_mongo}")

# Vérifier si toutes les lignes ont bien été insérées
if nb_lignes_pandas == nb_lignes_mongo:
    print("Toutes les lignes ont été insérées avec succès !")
else:
    print("Certaines lignes n'ont pas été insérées.")










# CREATE - Insérer un document
user1 = {"name": "Alice", "age": 30, "Gender": "Male"}
collection.insert_one(user1)  
print("Données insérées")

# READ - Lire les données
print("\n Tous les utilisateurs :")
for user1 in collection.find():
    print(user1)


# Vérifier la mise à jour
print(" Alice après mise à jour :", collection.find_one({"name": "Alice"}))


# UPDATE - Modifier un document
collection.update_one({"name": "Alice"}, {"$set": {"age": 31}})
print("\n Alice a été mise à jour")

# Vérifier la mise à jour
print(" Alice après mise à jour :", collection.find_one({"name": "Alice"}))


# DELETE - Supprimer un document
collection.delete_one({"name": "Alice"})
print("\ Alice a été supprimé")

# Vérifier la suppression
print("\n📌 Liste des utilisateurs après suppression :")
for user in collection.find():
    print(user)




