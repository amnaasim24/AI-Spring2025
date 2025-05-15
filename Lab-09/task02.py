import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_classification():
    data = {
        'email_content': [
            'Congratulations, you have won a free ticket!',
            'Hi team, please find the report attached.',
            'You have been selected for a cash prize.',
            'Meeting tomorrow at 10am.',
            'Buy now and get 50% off on all products.'
        ],
        'label': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['email_content'])
    y = df['label']

    model = MultinomialNB()
    model.fit(X, y)
    y_pred = model.predict(X)
    print("\n--- TASK 2: SPAM EMAIL CLASSIFICATION ---")
    print("Accuracy:", accuracy_score(y, y_pred))

    new_email = ["Claim your free reward by clicking this link!"]
    new_vec = vectorizer.transform(new_email)
    prediction = model.predict(new_vec)
    print("Is the new email spam?", 'Yes' if prediction[0] == 1 else 'No')

if __name__ == "__main__":
    spam_classification()