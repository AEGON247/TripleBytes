import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceDot } from 'recharts';

export const PredictionDisplay = ({ chartData, prediction, predictionIndex }) => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Stock Price Prediction</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="prices" stroke="#8884d8" name="Actual Price" />
            <Line type="monotone" dataKey="sentiment" stroke="#82ca9d" name="Sentiment" />

            {/* Highlight the predicted value */}
            <ReferenceDot x={predictionIndex} y={prediction} r={8} fill="red" label="Prediction" />
          </LineChart>
        </ResponsiveContainer>
        <div>
          <p><strong>Prediction:</strong> {prediction}</p>
        </div>
      </CardContent>
    </Card>
  );
};
