from flask import Flask, request, jsonify
import joblib
import numpy as np
import yfinance as yf

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('stock_predictor.pkl')  # Ensure the model file is in the same directory
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return "Stock Market Prediction API is running! changes"

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Get stock symbol from the request
    stock_symbol = data.get('symbol')

    if not stock_symbol:
        return jsonify({'error': 'Stock symbol is required!'}), 400

    # Download stock data using yfinance
    stock = yf.download(stock_symbol, period='1d')
    
    if stock.empty:
        return jsonify({'error': 'Invalid stock symbol or no data available.'}), 400

    # Prepare data for prediction (using features: 'Open', 'Close', 'High', 'Low', 'Volume')
    features = ['Open', 'Close', 'High', 'Low', 'Volume']
    stock_features = stock[features].values[-1].reshape(1, -1)  # Get the latest data

    # Scale the features using the pre-trained scaler
    stock_features_scaled = scaler.transform(stock_features)

    # Make the prediction (0 = down, 1 = up)
    prediction = model.predict(stock_features_scaled)[0]
    result = 'up' if prediction == 1 else 'down'

    # Return the prediction as a JSON response
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

