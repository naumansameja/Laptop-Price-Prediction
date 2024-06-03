from django.shortcuts import render 
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle

# Load the saved model


# Create your views here.
def home(request):
    return render(request, 'home.html')

def load_model():
    import os
    import pickle

    # Get the directory of the current Python script (models.py)
    current_dir = os.path.dirname(__file__)

    # Construct the path to the .pkl file relative to the current directory
    pkl_file_path = os.path.join(current_dir, 'laptop_price_model.pkl')

    # Load the pickled model
    with open(pkl_file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def laptop(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        operating_system = request.POST['operating_system']
        processor = request.POST['processor']
        
        # Extract numeric part of screen size and convert to float
        screen_size_str = request.POST['screen_size']
        screen_size_str = screen_size_str.split(' ')[0]  # Get only the numeric part before the first space
        try:
            screen_size = float(screen_size_str)
        except ValueError:
            screen_size = None  # If conversion fails, set to None

        # Extract numeric part of storage and RAM and convert to integers
        storage_str = request.POST['storage']
        storage_str = storage_str.split('GB')[0]  # Get only the numeric part before "GB"
        try:
            storage = int(storage_str)
        except ValueError:
            storage = None  # If conversion fails, set to None

        ram_str = request.POST['ram']
        ram_str = ram_str.split('GB')[0]  # Get only the numeric part before "GB"
        try:
            storage = int(storage_str)
        except ValueError:
            storage = None  # If conversion fails, set to None

        ram_str = request.POST['ram']
        ram_str = ram_str.split('GB')[0]  # Get only the numeric part before "GB"
        try:
            ram = int(ram_str)
        except ValueError:
            ram = None  # If conversion fails, set to None

        touch_screen = request.POST['touch_screen']

        # Load the model
        model = load_model()

        # Define the query data
        query_data = {
            'Brand': [brand],
            'Processor': [processor],
            'Operating System': [operating_system],
            'Storage': [storage],
            'RAM': [ram],
            'Screen Size': [screen_size],
            'Touch_Screen': [touch_screen]
        }

        # Convert the query data into a DataFrame
        query_df = pd.DataFrame(query_data)

        # Make predictions using the model
        predicted_log_price = model.predict(query_df)
        predicted_price = np.exp(predicted_log_price)

        return render(request, 'result.html', {'query_data': query_data, 'predicted_price': predicted_price*3.1})

    return render(request, 'laptop.html')


def result(request):
    return HttpResponse('Price is 1000')
