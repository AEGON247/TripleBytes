import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Download stock data (e.g., Apple stock)
stock = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
stock['Price Change'] = stock['Close'].shift(-1) > stock['Close']
stock.dropna(inplace=True)

# Features and target
features = ['Open', 'Close', 'High', 'Low', 'Volume']
X = stock[features]
y = stock['Price Change'].astype(int)  # 1 for price goes up, 0 for price goes down

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the trained model and scaler
joblib.dump(model, 'stock_predictor.pkl')
joblib.dump(scaler, 'scaler.pkl')

print(f'Model saved with accuracy: {model.score(X_test_scaled, y_test):.2f}')
