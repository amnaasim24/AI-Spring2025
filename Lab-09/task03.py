import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def customer_value():
    data = {
        'spending': [5000, 200, 7000, 300, 10000],
        'age': [25, 30, 45, 23, 35],
        'visits': [20, 2, 30, 1, 40],
        'frequency': [5, 1, 6, 1, 8],
        'label': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    X = df[['spending', 'age', 'visits', 'frequency']]
    y = df['label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\n--- TASK 3: CUSTOMER VALUE CLASSIFICATION ---")
    print(classification_report(y_test, y_pred))

    tree = DecisionTreeClassifier()
    tree.fit(X, y)
    print("Feature Importances:", tree.feature_importances_)

if __name__ == "__main__":
    customer_value()