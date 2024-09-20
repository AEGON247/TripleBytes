import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Fetch stock data
def fetch_stock_data(ticker, period='20y'):
    stock_data = yf.download(ticker, period=period)
    return stock_data

# Prepare data for prediction
def prepare_data(df):
    # Create percentage change as a feature
    df['Pct_Change'] = df['Adj Close'].pct_change()
    
    # Target: 1 if price goes up, 0 if price goes down
    df['Target'] = (df['Pct_Change'].shift(-1) > 0).astype(int)
    
    # Remove NaN values created by shifting
    df = df.dropna()
    
    # Features: percentage change, Target: whether price went up
    X = df[['Pct_Change']]
    y = df['Target']
    
    return X, y

# Train the model and predict
def predict_stock_movement(ticker):
    # Step 1: Fetch stock data
    stock_data = fetch_stock_data(ticker)
    
    # Step 2: Prepare the data
    X, y = prepare_data(stock_data)
    
    # Step 3: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Step 4: Train a Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Step 5: Make predictions
    y_pred = model.predict(X_test)
    
    # Step 6: Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    # Return predictions
    stock_data['Prediction'] = None
    stock_data.iloc[-len(y_test):, stock_data.columns.get_loc('Prediction')] = y_pred
    
    return stock_data.tail()

# Example usage:
ticker = 'GOOG'  # Apple Inc.
predicted_data = predict_stock_movement(ticker)
print(predicted_data)