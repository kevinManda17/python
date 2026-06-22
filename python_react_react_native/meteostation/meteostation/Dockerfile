# Dockerfile
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier requirements.txt et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Exposer le port
EXPOSE 8000

# Commande par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
