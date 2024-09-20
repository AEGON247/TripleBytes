# models.py
import pandas as pd
import requests
from textblob import TextBlob
import sqlite3

def fetch_data(ticker):
    api_key = 'bce53d4df6cf4bfdbdef27ed7564a13c'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}'
    response = requests.get(url).json()
    
    if 'Error Message' in response:
        raise ValueError(f"Error fetching data for {ticker}: {response['Error Message']}")
    
    prices = pd.DataFrame(response['Time Series (Daily)']).T
    prices = prices.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close'})
    prices['Close'] = prices['Close'].astype(float)
    return prices

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def predict_sentiment(ticker):
    prices = fetch_data(ticker)
    sentiment_score = analyze_sentiment("Sample news related to stock")
    prediction = "Positive" if sentiment_score > 0 else "Negative"
         
    chart_data = {
        'labels': prices.index.tolist(),
        'prices': prices['Close'].tolist(),
        'sentiment': [sentiment_score] * len(prices)
    }
    return prediction, chart_data

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stocks (ticker TEXT, date TEXT, price REAL)')
    conn.commit()
    conn.close()
