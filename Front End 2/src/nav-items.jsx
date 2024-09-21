import { HomeIcon } from "lucide-react";
import Index from "./pages/Index.jsx";
import StockPrediction from "./components/StockPrediction";  // Import the StockPrediction component

/**
 * Central place for defining the navigation items. Used for navigation components and routing.
 */
export const navItems = [
  {
    title: "Home",
    to: "/",
    icon: <HomeIcon className="h-4 w-4" />,
    page: <Index />,
  },
  {
    title: "Stock Prediction",  // New item for Stock Prediction
    to: "/stock-prediction",  // Route path for Stock Prediction page
    icon: <HomeIcon className="h-4 w-4" />,  // You can change this icon to something else if desired
    page: <StockPrediction />,  // Component to render when the route is visited
  },
];
