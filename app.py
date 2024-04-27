from flask_cors import CORS
from flask import Flask, request, jsonify, send_file


app = Flask(__name__)

# Allow CORS for the specific origin
CORS(app, origins="http://127.0.0.1:5500")

import joblib

# Load the model using joblib
model = joblib.load('random_forest_model.pkl')



@app.route('/')
def home():
    return send_file('run.html')



@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    
    # Initialize a list for inputs
    inputs = []
    
    # Collect `simulationRun` and `sample` values
    # Convert them to floats and use default values if necessary
    simulation_run = data.get('simulationRun', '')
    if simulation_run == '':
        inputs.append(1)  # Default value for `simulationRun`
    else:
        inputs.append(float(simulation_run))
    
    sample = data.get('sample', '')
    if sample == '':
        inputs.append(1)  # Default value for `sample`
    else:
        inputs.append(float(sample))
    
    # Convert inputs for `xmeas_1` to `xmeas_41`
    for i in range(41):
        value = data.get(f'xmeas_{i + 1}', '')
        if value == '':
            inputs.append(500)  # Default to 0.5 if value is an empty string
        else:
            inputs.append(float(value))
    
    # Convert inputs for `xmv_1` to `xmv_11`
    for i in range(11):
        value = data.get(f'xmv_{i + 1}', '')
        if value == '':
            inputs.append(500)  # Default to 0.5 if value is an empty string
        else:
            inputs.append(float(value))
    
    # Make the prediction
    prediction = model.predict([inputs])[0]
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
