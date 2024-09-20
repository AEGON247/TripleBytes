import pandas as pd

def load_stock_data(ticker):
    # Load your stock price data (e.g., from a CSV or API)
    df = pd.read_csv(f"{ticker}_prices.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

def preprocess_sentiment_data(sentiment_df):
    # Clean and preprocess the sentiment data
    sentiment_df['text'] = sentiment_df['text'].str.lower()  # Example preprocessing
    return sentiment_df

from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a score between -1 and 1

def apply_sentiment_analysis(sentiment_df):
    sentiment_df['sentiment'] = sentiment_df['text'].apply(analyze_sentiment)
    return sentiment_df

def merge_data(prices, sentiments):
    merged_data = prices.join(sentiments.set_index('date'))  # Assuming 'date' column exists
    merged_data.dropna(inplace=True)  # Handle missing values
    return merged_data

def create_features(data):
    data['MA_5'] = data['close'].rolling(window=5).mean()  # 5-day moving average
    data['MA_20'] = data['close'].rolling(window=20).mean()  # 20-day moving average
    return data

from sklearn.model_selection import train_test_split

def prepare_data(data):
    X = data[['MA_5', 'MA_20', 'sentiment']]  # Features
    y = data['close'].shift(-1)  # Predict next day's closing price
    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

def print_evaluation(mse):
    print(f'Mean Squared Error: {mse}')

import joblib

def save_model(model):
    joblib.dump(model, 'stock_model.pkl')

def load_model():
    return joblib.load('stock_model.pkl')


