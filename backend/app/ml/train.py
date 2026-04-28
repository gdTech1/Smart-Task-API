import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/tasks_dataset.csv")

X = df["text"]
y = df["priority"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

with open("backend/app/ml/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Modelo treinado!")