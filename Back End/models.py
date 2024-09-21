# models.py
import pandas as pd
import requests
from textblob import TextBlob
import sqlite3
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Fetch stock data from the Alpha Vantage API
def fetch_data(ticker):
    api_key = 'KSUSMLIBH7MMNYNN'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}'
    response = requests.get(url).json()
    
    if 'Error Message' in response:
        raise ValueError(f"Error fetching data for {ticker}: {response['Error Message']}")
    
    prices = pd.DataFrame(response['Time Series (Daily)']).T
    prices = prices.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close'})
    prices['Close'] = prices['Close'].astype(float)
    prices.index = pd.to_datetime(prices.index)  # Convert index to DateTime
    return prices

# Analyze the sentiment using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Process sentiment data
def preprocess_sentiment_data(sentiment_df):
    sentiment_df['text'] = sentiment_df['text'].str.lower()  # Convert text to lowercase
    return sentiment_df

# Apply sentiment analysis to the sentiment dataset
def apply_sentiment_analysis(sentiment_df):
    sentiment_df['sentiment'] = sentiment_df['text'].apply(analyze_sentiment)
    return sentiment_df

# Merge stock prices and sentiment data
def merge_data(prices, sentiments):
    merged_data = prices.join(sentiments.set_index('date'))  # Assuming 'date' column exists in sentiments
    merged_data.dropna(inplace=True)  # Handle missing values
    return merged_data

# Create features from the data (e.g., moving averages)
def create_features(data):
    data['MA_5'] = data['Close'].rolling(window=5).mean()  # 5-day moving average
    data['MA_20'] = data['Close'].rolling(window=20).mean()  # 20-day moving average
    return data

# Split data into training and test sets
def prepare_data(data):
    X = data[['MA_5', 'MA_20', 'sentiment']]  # Features: moving averages and sentiment score
    y = data['Close'].shift(-1)  # Predict next day's closing price
    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train a random forest model
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    return model

# Evaluate the model with Mean Squared Error (MSE)
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Save the trained model to a file
def save_model(model):
    joblib.dump(model, 'stock_model.pkl')

# Load a pre-trained model from a file
def load_model():
    return joblib.load('stock_model.pkl')

# Main prediction function that ties everything together
def predict_sentiment(ticker):
    # Step 1: Fetch stock prices
    prices = fetch_data(ticker)
    
    # Step 2: Fetch and analyze sentiment data (you can replace this with real news data)
    sentiment_df = pd.DataFrame({'date': prices.index, 'text': ['Sample news' for _ in range(len(prices))]})
    sentiments = apply_sentiment_analysis(sentiment_df)

    # Step 3: Merge stock and sentiment data
    data = merge_data(prices, sentiments)
    data = create_features(data)

    # Step 4: Prepare data for model training
    X_train, X_test, y_train, y_test = prepare_data(data)

    # Step 5: Train model or load existing model
    if os.path.exists('stock_model.pkl'):
        model = load_model()
    else:
        model = train_model(X_train, y_train)
        save_model(model)

    # Step 6: Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Model Evaluation - MSE: {mse}")

    # Step 7: Make predictions
    prediction = model.predict(X_test[-1:])[0]
    
    # Step 8: Create chart data for the frontend
    chart_data = {
        'labels': prices.index.tolist(),
        'prices': prices['Close'].tolist(),
        'sentiment': sentiments['sentiment'].tolist()
    }

    return prediction, chart_data

# Initialize the database (optional if you want to save data locally)
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stocks (ticker TEXT, date TEXT, price REAL)')
    conn.commit()
    conn.close()
