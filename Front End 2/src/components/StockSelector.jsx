import React, { useState } from 'react';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const stockOptions = [
  { value: 'AAPL', label: 'Apple Inc. (AAPL)' },
  { value: 'GOOGL', label: 'Alphabet Inc. (GOOGL)' },
  { value: 'MSFT', label: 'Microsoft Corporation (MSFT)' },
  { value: 'AMZN', label: 'Amazon.com Inc. (AMZN)' },
  { value: 'FB', label: 'Meta Platforms Inc. (FB)' },
];

export const StockSelector = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const filteredOptions = stockOptions.filter(option =>
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Select a Stock</h2>
      <Select>
        <SelectTrigger className="w-full">
          <SelectValue placeholder="Choose a stock" />
        </SelectTrigger>
        <SelectContent>
          <input
            type="text"
            placeholder="Search stocks..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="mb-2 p-2 border rounded"
          />
          {filteredOptions.map((option) => (
            <SelectItem key={option.value} value={option.value}>
              {option.label}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
};
