document.getElementById('predict-btn').addEventListener('click', () => {
    const stockSymbol = document.getElementById('stock-symbol').value;
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ symbol: stockSymbol }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            document.getElementById('result').textContent = `Prediction: Stock will go ${data.prediction}.`;
        } else if (data.error) {
            document.getElementById('result').textContent = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        document.getElementById('result').textContent = 'Error fetching prediction.';
        console.error('Error:', error);
    });
});
