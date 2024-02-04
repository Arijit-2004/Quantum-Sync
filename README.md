# Fraud Detection Website

## Overview

This repository contains the code for a fraud detection website developed by a team of four individuals. The website is designed to detect fraudulent activities using a Support Vector Machine (SVM) model implemented in scikit-learn. The frontend of the website is built with HTML, CSS, and JavaScript, while the backend is powered by Flask.

## Features

- **User-friendly Interface:** The website provides a simple and intuitive interface for users to interact with the fraud detection system.

- **Real-time Prediction:** Users can input relevant data, and the SVM model will provide a real-time prediction regarding the likelihood of fraud.

- **Visualizations:** The website includes visualizations to help users understand the data and the model's predictions better.

## Technologies Used

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Flask

- **Machine Learning Model:**
  - SVM (Support Vector Machine) from scikit-learn

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/fraud-detection-website.git
   cd fraud-detection-website
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python app.py
   ```
   The website will be accessible at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

2. Input relevant data into the provided fields.

3. Click on the "Predict" button to get predictions.

4. Explore visualizations and results provided by the website.

## Project Structure

```
fraud-detection-website/
|-- static/
|   |-- css/
|   |-- js/
|   |-- images/
|-- templates/
|-- app.py
|-- model/
|-- README.md
|-- requirements.txt
```

- **static:** Contains static files such as CSS, JavaScript, and images.
- **templates:** Holds HTML templates used by Flask to render pages.
- **app.py:** Flask application file.
- **model:** Contains the trained SVM model.

## Contributors

- Arijit Chatterjee (https://github.com/Arijit-2004)
- Sagnik Basak (https://github.com/SagnikBasak04)
- Anidipta Pal(https://github.com/Anidipta)
- Ayan Dasgupta(https://github.com/AD9190)

## Acknowledgments

We would like to express our gratitude to IEM to give us a platform to create this website 

Feel free to contribute, report issues, or provide feedback to help us improve this project.
