from sklearn.linear_model import LinearRegression
import numpy as np

# Données d'entraînement (X: entrée, y: sortie)
# y = 3*x + 2 (on veut que le modèle apprenne ça)
X = np.array([[1], [2], [3], [4], [5]])  # Entrées
y = np.array([5, 8, 11, 14, 17])        # Sorties (vraies)

# Créer un modèle de régression linéaire
model = LinearRegression()

# 🎯 Etape d'ENTRAÎNEMENT : on apprend les paramètres à partir des données
model.fit(X, y)

# Récupérer les paramètres appris
poids = model.coef_       # Le poids (w)
biais = model.intercept_  # Le biais (b)

print("Poids appris (w):", poids)
print("Biais appris (b):", biais)

# 🔮 Utiliser le modèle pour prédire
X_test = np.array([[6]])
y_pred = model.predict(X_test)
print("Prédiction pour x=6 :", y_pred)


help(LinearRegression)