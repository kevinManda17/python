# station/management/commands/train_model.py

from django.core.management.base import BaseCommand
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

MODEL_DIR = "station/ml/model_store"
MODEL_FILE = os.path.join(MODEL_DIR, "latest_model.joblib")

class Command(BaseCommand):
    help = "Entraîne un modèle météo depuis un CSV Kaggle et sauvegarde le modèle."

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            type=str,
            required=True,
            help="Chemin vers le CSV"
        )

    def handle(self, *args, **options):
        csv_path = options["csv"]

        try:
            df = pd.read_csv(csv_path)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Fichier non trouvé : {csv_path}"))
            return

        # Colonnes à utiliser pour le modèle
        feature_columns = ['humidity', 'pressure_mb', 'wind_kph']
        target_column = 'temperature_celsius'

        # Vérifier que toutes les colonnes existent
        missing_cols = [c for c in feature_columns + [target_column] if c not in df.columns]
        if missing_cols:
            self.stderr.write(self.style.ERROR(f"Colonnes manquantes dans le CSV : {missing_cols}"))
            return

        # Supprimer les lignes avec valeurs manquantes
        df = df.dropna(subset=feature_columns + [target_column])

        X = df[feature_columns]
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump(model, MODEL_FILE)

        score = model.score(X_test, y_test)
        self.stdout.write(self.style.SUCCESS(
            f"Modèle entraîné et sauvegardé dans {MODEL_FILE} (R*R = {score:.3f})"
        ))
