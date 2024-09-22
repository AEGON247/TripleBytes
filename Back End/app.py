# app.py
from flask import Flask, request, jsonify
from models import fetch_data, predict_sentiment
from flask_cors import CORS
     
app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400
    
    # Get prediction, chart data, and the prediction index
    prediction, chart_data, prediction_index = predict_sentiment(ticker)
    
    # Return the data in a structured format to the frontend
    return jsonify({
        'prediction': prediction, 
        'chartData': chart_data, 
        'predictionIndex': prediction_index
    })


if __name__ == '__main__':
    app.run(debug=True)
