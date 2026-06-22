import joblib
import numpy as np

class EnergyPredictor:
    def __init__(self):
        self.model = joblib.load('ml/energy_model.pkl')

    def predict(self, input_data: dict):
        X = np.array([list(input_data.values())])
        return self.model.predict(X)[0]
