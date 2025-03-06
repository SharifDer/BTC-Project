# Crypto Price Prediction with RandomForestClassifier

## Overview
This project applies machine learning to predict cryptocurrency price movements using a RandomForestClassifier. We calculate various technical indicators and classify price changes into two categories: 0 or 1.
The data was fectched from binance api so they are real world data.
## Key Features
- Extracts moving averages (SMA, EMA, WMA) and other indicators like ATR, VWMA, Momentum, and CCI.
- Uses historical price data to classify price movement into two classes (0 or 1).
- Passes the targeted value from the previous record to the current record for prediction.
- Splits data for training and testing using a time-series approach.
- Implements hyperparameter tuning to select the best classification model.

## Model Training
- Uses a RandomForestClassifier with different criteria (entropy, gini) to find the best accuracy.
- Evaluates the model using accuracy score and confusion matrix.

## Results
- Outputs predictions alongside actual values for comparison.
- Displays model accuracy and the maximum depth reached by decision trees in the Random Forest.
- 
## Dependencies
To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt

## Usage
Run the script to preprocess data, train the model, and generate predictions.



