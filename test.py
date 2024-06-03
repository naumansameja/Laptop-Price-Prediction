import pickle
import numpy as np
import pandas as pd

# Load the model and feature names
with open('laptop_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define your query data as a dictionary with feature names
query_data = {
    'Brand': ['HP'],
    'Processor': ['Core i5'],
    'Operating System': ['Windows'],
    'Storage': [512],
    'RAM': [8],
    'Screen Size': [39.82],
    'Touch_Screen': ['No']
}

# Convert the query data into a DataFrame
query_df = pd.DataFrame(query_data)

# Make predictions using the model
predicted_log_price = model.predict(query_df)
predicted_price = np.exp(predicted_log_price)

print("Predicted price:", predicted_price)
