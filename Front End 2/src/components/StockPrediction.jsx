import React, { useState } from "react";
import { StockDataInput } from "./StockDataInput";
import { PredictionDisplay } from "./PredictionDisplay";
import axios from "axios";

const StockPrediction = () => {
  const [ticker, setTicker] = useState("");    // Store user inputted ticker
  const [predictionData, setPredictionData] = useState(null);  // Store the prediction data
  const [error, setError] = useState(null);    // Store error messages

  const handleFetchPrediction = async () => {
    try {
      if (!ticker) {
        alert("Please enter a stock ticker!");
        return;
      }
      const response = await axios.get(
        `http://localhost:5000/api/predict?ticker=${ticker}`
      );
      setPredictionData(response.data);  // Set data from backend into predictionData
    } catch (err) {
      setError("Error fetching prediction data. Please try again.");
    }
  };

  return (
    <div className="stock-prediction">
      <h1>Stock Prediction</h1>
      
      {/* Stock selector input */}
      <input
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="Enter Stock Ticker (e.g., AAPL)"
        className="border p-2 rounded mb-4"
      />

      {/* Predict Button */}
      <button 
        onClick={handleFetchPrediction} 
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
      >
        Predict
      </button>

      {/* Display error message if there's an error */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Display chart with prediction data */}
      {predictionData && (
        <PredictionDisplay
          chartData={predictionData.chartData}
          prediction={predictionData.prediction}
        />
      )}
    </div>
  );
};

export default StockPrediction;
