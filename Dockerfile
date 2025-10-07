# Étape 1 : image de base
FROM python:3.11-slim

# Étape 2 : dossier de travail
WORKDIR /app

# Étape 3 : copie des fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY main.py .

# Étape 4 : port exposé
EXPOSE 8000

# Étape 5 : commande de démarrage
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
