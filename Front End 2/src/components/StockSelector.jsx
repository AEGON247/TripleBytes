import React from 'react';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

export const StockSelector = () => {
  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Select a Stock</h2>
      <Select>
        <SelectTrigger className="w-full">
          <SelectValue placeholder="Choose a stock" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="AAPL">Apple Inc. (AAPL)</SelectItem>
          <SelectItem value="GOOGL">Alphabet Inc. (GOOGL)</SelectItem>
          <SelectItem value="MSFT">Microsoft Corporation (MSFT)</SelectItem>
          <SelectItem value="AMZN">Amazon.com Inc. (AMZN)</SelectItem>
          <SelectItem value="FB">Meta Platforms Inc. (FB)</SelectItem>
        </SelectContent>
      </Select>
    </div>
  );
};