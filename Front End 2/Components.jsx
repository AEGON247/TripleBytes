import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const dummyData = [
  { name: 'Day 1', actual: 4000, predicted: 4100 },
  { name: 'Day 2', actual: 4200, predicted: 4300 },
  { name: 'Day 3', actual: 4100, predicted: 4000 },
  { name: 'Day 4', actual: 4400, predicted: 4500 },
  { name: 'Day 5', actual: 4300, predicted: 4400 },
];

export const PredictionDisplay = () => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Stock Price Prediction</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={dummyData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="actual" stroke="#8884d8" name="Actual Price" />
            <Line type="monotone" dataKey="predicted" stroke="#82ca9d" name="Predicted Price" />
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
};