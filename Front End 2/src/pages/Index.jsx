import React from 'react';
import { StockSelector } from '../components/StockSelector';
import { StockDataInput } from '../components/StockDataInput';
import { PredictionDisplay } from '../components/PredictionDisplay';

const Index = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-4xl font-bold mb-8 text-center">Stock Market Prediction</h1>
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">
        <StockSelector />
        <StockDataInput />
        <PredictionDisplay />
      </div>
    </div>
  );
};

export default Index;
