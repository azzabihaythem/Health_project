# Health_project

**1-create file .env**

```env
MONGO_ADMIN_USERNAME=*****
MONGO_READ_ONLY_USERNAME=*****
MONGO_ADMIN_PASSWORD=*****
MONGO_READ_ONLY_USERNAME_PASSWORD=*****
MONGO_HOST=mongo
MONGO_PORT=27017
```

**2 - Run**


Lancer la commande suivante dans PowerShell pour démarrer les services via Docker :


```bash
docker-compose up --build   
```

**3- Interface MongoDB**

Open Studio 3T and connect to database via user and password




# DETAILS DU PROJET 

**Description**


Ce projet permet l'importation, le nettoyage, l'insertion et la validation de données de patients dans une base de données MongoDB à partir d'un fichier CSV. Il comprend un service MongoDB et un service Python pour exécuter les scripts d'analyse et de test

**Structure du Projet**

├── docker-compose.yml
├── Dockerfile
├── python/
│   ├── healthVisual.py
│   ├── testVisual.py
├── csv/
│   ├── healthcare_dataset_nettoye.csv
├── requirements.txt
└── README.md
Prérequis
•	Docker et Docker Compose
•	Python 3.10+
•	MongoDB

**Installation**
1.	Cloner le dépôt :
2.	git clone <URL_REPO>
cd <NOM_DU_PROJET>
3.	Installer les dépendances Python :
pip install -r requirements.txt

**Exécution avec Docker**

1.	Démarrer les services :
docker-compose up --build
2.	Les scripts Python s'exécutent automatiquement et procèdent à :
o	Chargement et nettoyage des données CSV
o	Insertion dans MongoDB
o	Validation de l'importation avec des tests unitaires
3.	Arrêter les services :
docker-compose down

**Scripts Principaux:**

***healthVisual.py***

•	Charge les données depuis le fichier CSV
•	Effectue le nettoyage des données
•	Convertit certains champs en formats compatibles avec MongoDB
•	Insère les données dans la collection patients
•	Affiche des statistiques sur l'insertion
MongoDB - Opérations CRUD
•	Create : Insérer un document
•	Read : Récupérer des données
•	Update : Modifier un document
•	Delete : Supprimer un document

***testVisual.py***

•	Teste la correspondance entre les données du fichier CSV et MongoDB

•	Vérifie :
o	L'égalité du nombre de lignes
o	La cohérence du nombre de colonnes
•	Effectue des tests unitaires avec unittest


**Variables d'Environnement**
Les identifiants de connexion MongoDB sont définis dans docker-compose.yml :

  environment:
    - MONGO_INITDB_ROOT_USERNAME=admin
    - MONGO_INITDB_ROOT_PASSWORD=admin#75*Db


***Améliorations Possibles***

•	Ajouter un fichier de configuration .env
•	Implémenter une interface web pour visualiser les données
•	Améliorer la gestion des erreurs et des logs


Remarque : Le fichier README.md ne sera pas transféré à Github

