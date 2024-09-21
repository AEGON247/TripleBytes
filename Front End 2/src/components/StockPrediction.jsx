import React, { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const fetchPrediction = async (ticker) => {
  const response = await axios.get(`http://localhost:5000/api/predict?ticker=${ticker}`);
  return response.data;
};

const StockPrediction = () => {
  const [ticker, setTicker] = useState("");
  const { data, error, isLoading, refetch } = useQuery(
    ["stockPrediction", ticker],
    () => fetchPrediction(ticker),
    {
      enabled: false,  // Disable auto-fetch until refetch is called
    }
  );

  const handleFetchPrediction = () => {
    if (ticker) {
      refetch();  // Trigger fetching the data
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

      {isLoading && <p>Loading...</p>}
      {error && <p>Error fetching prediction.</p>}
      {data && (
        <div>
          <h2>Prediction: {data.prediction}</h2>
          {/* Display chartData or other results here */}
        </div>
      )}
    </div>
  );
};

export default StockPrediction;
