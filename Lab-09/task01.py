import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def house_price_prediction():
    data = {
        'sqft': [1500, 2000, 1800, 2400, 3000],
        'bedrooms': [3, 4, 3, 5, 4],
        'bathrooms': [2, 3, 2, 4, 3],
        'age': [10, 5, 15, 8, 3],
        'neighborhood': ['A', 'B', 'A', 'C', 'B'],
        'price': [300000, 400000, 350000, 500000, 450000]
    }
    df = pd.DataFrame(data)
    df['neighborhood'] = df['neighborhood'].astype('category').cat.codes

    features = ['sqft', 'bedrooms', 'bathrooms', 'age', 'neighborhood']
    X = df[features]
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\n--- TASK 1: HOUSE PRICE PREDICTION ---")
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

    new_house = [[2000, 3, 2, 10, 1]]
    prediction = model.predict(new_house)
    print("Predicted Price for new house:", prediction[0])

if __name__ == "__main__":
    house_price_prediction()