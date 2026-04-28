import pickle

with open("app/ml/model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)


def predict_priority(text: str):
    X = vectorizer.transform([text])
    return model.predict(X)[0]