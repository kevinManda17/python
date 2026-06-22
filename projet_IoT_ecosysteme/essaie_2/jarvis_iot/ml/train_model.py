import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data_path='ml/data.csv'):
    df = pd.read_csv(data_path)
    X = df.drop(columns=['consumption'])
    y = df['consumption']
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    joblib.dump(model, 'ml/energy_model.pkl')
    return model
