import React, { useState } from 'react';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import axios from "axios";  // Import axios for making API calls

export const StockDataInput = ({ setPredictionData }) => {
  const [formData, setFormData] = useState({
    opening: '',
    closing: '',
    high: '',
    low: '',
    volume: '',
  });

  // Function to handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Function to handle form submission and make API call
  const handleSubmit = async () => {
    try {
      const { data } = await axios.get(
        `http://localhost:5000/api/predict?ticker=MSFT`  // Replace ticker accordingly
      );
      setPredictionData(data);  // Pass the received data to parent component
    } catch (error) {
      console.error("Error fetching prediction:", error);
    }
  };

  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Enter Stock Data</h2>
      <div className="grid grid-cols-2 gap-4">
        <Input
          name="opening"
          type="number"
          value={formData.opening}
          onChange={handleChange}
          placeholder="Opening Price"
        />
        <Input
          name="closing"
          type="number"
          value={formData.closing}
          onChange={handleChange}
          placeholder="Closing Price"
        />
        <Input
          name="high"
          type="number"
          value={formData.high}
          onChange={handleChange}
          placeholder="High"
        />
        <Input
          name="low"
          type="number"
          value={formData.low}
          onChange={handleChange}
          placeholder="Low"
        />
        <Input
          name="volume"
          type="number"
          value={formData.volume}
          onChange={handleChange}
          placeholder="Volume"
        />
      </div>
      <Button className="mt-4 w-full" onClick={handleSubmit}>
        Predict
      </Button>
    </div>
  );
};
