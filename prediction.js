function predictFraud() {
    // Fetch input values
    const transactionType = document.getElementById('transactionType').value;
    const step = document.getElementById('step').value;
    const moneyDifference = document.getElementById('moneyDifference').value;
    // const sender = document.getElementById('sender').value;
    // const receiver = document.getElementById('receiver').value;

    // Send input to Flask server
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            transactionType,
            step,
            moneyDifference,
            // sender,
            // receiver,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        document.getElementById('predictionResult').innerText = `Prediction: ${data.result}`;
    })
    .catch(error => console.error('Error:', error));
}