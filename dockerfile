 # Utiliser une image officielle de Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
#COPY <source> <destination>
#  The Destination (.) refers to the current working directory 
#inside the container, which is /app (set by WORKDIR /app).

COPY requirements.txt .

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY /python/testVisual.py .


# Copier le reste des fichiers dans le conteneur
COPY /python/healthVisual.py .



# Commande par défaut pour exécuter le script Python
#Couldn't be executed beause the volume (/data/csv)is not reachable yet
#CMD ["python", "healthVisual.py"]
