import pandas as pd
import numpy as np

print("Début du programme...")

# Reproductibilité
np.random.seed(42)

# Nombre de clients
n = 500

# Génération des données
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "salaire": np.random.randint(1200, 8000, n),
    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),
    "anciennete": np.random.randint(0, 15, n),
    "consommation": np.random.randint(0, 100, n)
})

# Création de la variable cible
data["churn"] = (
    (data["consommation"] < 30)
    & (data["anciennete"] < 2)
).astype(int)

# Sauvegarde
data.to_csv("churn_data.csv", index=False)

# Vérifications
print("\nPremières lignes :")
print(data.head())

print(f"\nNombre de lignes : {len(data)}")
print(f"Nombre de colonnes : {len(data.columns)}")
print(f"Taux de churn : {data['churn'].mean():.1%}")

print("\nFichier CSV créé avec succès !")
