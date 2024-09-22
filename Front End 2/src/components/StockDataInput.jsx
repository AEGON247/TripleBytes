import React, { useState, useEffect } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export const StockDataInput = ({ ticker }) => {
  const [stockData, setStockData] = useState(null);

  useEffect(() => {
    // Fetch stock data automatically when ticker changes
    const fetchStockData = async () => {
      if (ticker) {
        try {
          const response = await axios.get(`http://localhost:5000/api/predict?ticker=${ticker}`);
          setStockData(response.data.chartData);  // Set stock data from API
        } catch (err) {
          console.error("Error fetching stock data:", err);
        }
      }
    };

    fetchStockData();
  }, [ticker]);  // Only re-fetch data when the ticker changes

  if (!stockData) return null;

  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Recent Stock Data for {ticker}</h2>
      <div className="grid grid-cols-2 gap-4">
        <Input
          value={stockData.opening || ""}
          readOnly
          placeholder="Opening Price"
          className="border p-2 rounded"
        />
        <Input
          value={stockData.closing || ""}
          readOnly
          placeholder="Closing Price"
          className="border p-2 rounded"
        />
        <Input
          value={stockData.high || ""}
          readOnly
          placeholder="High"
          className="border p-2 rounded"
        />
        <Input
          value={stockData.low || ""}
          readOnly
          placeholder="Low"
          className="border p-2 rounded"
        />
        <Input
          value={stockData.volume || ""}
          readOnly
          placeholder="Volume"
          className="border p-2 rounded"
        />
      </div>
    </div>
  );
};
