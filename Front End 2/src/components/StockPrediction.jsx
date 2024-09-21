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
      <input
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="Enter Stock Ticker (e.g., AAPL)"
      />
      <button onClick={handleFetchPrediction}>Get Prediction</button>

      {/* Display error message if there's an error */}
      {error && <p>{error}</p>}

      {/* Display stock input form */}
      <StockDataInput setPredictionData={setPredictionData} ticker={ticker} />

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
