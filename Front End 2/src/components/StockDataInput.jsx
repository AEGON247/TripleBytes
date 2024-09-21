import React from 'react';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export const StockDataInput = () => {
  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Enter Stock Data</h2>
      <div className="grid grid-cols-2 gap-4">
        <Input type="number" placeholder="Opening Price" />
        <Input type="number" placeholder="Closing Price" />
        <Input type="number" placeholder="High" />
        <Input type="number" placeholder="Low" />
        <Input type="number" placeholder="Volume" />
      </div>
      <Button className="mt-4 w-full">Predict</Button>
    </div>
  );
};