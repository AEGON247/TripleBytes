import { fileURLToPath, URL } from "url";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: "::",  // Keep this to allow external access (if needed)
    port: "8080",  // Frontend will run on port 8080
    proxy: {
      // Proxy API requests to the Flask backend running on port 5000
      '/api': {
        target: 'http://localhost:5000',  // Backend running on port 5000
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),  // Optional: If Flask routes are already prefixed with /api
      },
    },
  },
  plugins: [react()],
  resolve: {
    alias: [
      {
        find: "@",
        replacement: fileURLToPath(new URL("./src", import.meta.url)),
      },
      {
        find: "lib",
        replacement: resolve(__dirname, "lib"),
      },
    ],
  },
});
