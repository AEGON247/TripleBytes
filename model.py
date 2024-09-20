# models.py
import pandas as pd
import requests

def fetch_data(ticker):
    # Example of fetching historical stock prices using Alpha Vantage API
    api_key = 'YOUR_API_KEY'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}'
    response = requests.get(url).json()
    prices = pd.DataFrame(response['Time Series (Daily)']).T
    prices = prices.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close'})
    prices['Close'] = prices['Close'].astype(float)
    return prices

from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def predict_sentiment(ticker):
    # Fetch data
    prices = fetch_data(ticker)
    # Analyze sentiment for your data (e.g., news or tweets related to the stock)
    # Example sentiment data, replace with actual sentiment analysis
    sentiment_score = analyze_sentiment("Sample news related to stock")
    prediction = "Positive" if sentiment_score > 0 else "Negative"
         
    # Prepare chart data
    chart_data = {
        'labels': prices.index.tolist(),
        'prices': prices['Close'].tolist(),
        'sentiment': [sentiment_score] * len(prices)
    }
    return prediction, chart_data

@app.route('/api/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400
    try:
        prediction, chart_data = predict_sentiment(ticker)
        return jsonify({'prediction': prediction, 'chartData': chart_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
