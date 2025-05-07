FROM python:3.9

# Installer pip et les outils utiles
RUN apt-get update && apt-get install -y curl git

# Installer les packages Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    jupyterlab ipykernel

# Créer un répertoire de travail
WORKDIR /app

