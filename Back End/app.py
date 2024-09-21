# app.py
from flask import Flask, request, jsonify
from models import fetch_data, predict_sentiment
     
app = Flask(__name__)

@app.route('/api/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400
    prediction, chart_data = predict_sentiment(ticker)
    return jsonify({'prediction': prediction, 'chartData': chart_data})

if __name__ == '__main__':
    app.run(debug=True)
