import requests

# Define the URL of your Flask API endpoint
url = 'http://localhost:5000/predict'

# Define the input data as a JSON object
data = {
    "simulationRun": 1,
    "sample": 1,
    "xmeas_1": 500,
    "xmeas_2": 500,
    "xmeas_3": 500,
    "xmeas_4": 500,
    "xmeas_5": 500,
    "xmeas_6": 500,
    "xmeas_7": 500,
    "xmeas_8": 500,
    "xmeas_9": 500,
    "xmeas_10": 500,
    "xmeas_11": 500,
    "xmeas_12": 500,
    "xmeas_13": 500,
    "xmeas_14": 500,
    "xmeas_15": 500,
    "xmeas_16": 500,
    "xmeas_17": 500,
    "xmeas_18": 500,
    "xmeas_19": 500,
    "xmeas_20": 500,
    "xmeas_21": 500,
    "xmeas_22": 500,
    "xmeas_23": 500,
    "xmeas_24": 500,
    "xmeas_25": 500,
    "xmeas_26": 500,
    "xmeas_27": 500,
    "xmeas_28": 500,
    "xmeas_29": 500,
    "xmeas_30": 500,
    "xmeas_31": 500,
    "xmeas_32": 500,
    "xmeas_33": 500,
    "xmeas_34": 500,
    "xmeas_35": 500,
    "xmeas_36": 500,
    "xmeas_37": 500,
    "xmeas_38": 500,
    "xmeas_39": 500,
    "xmeas_40": 500,
    "xmeas_41": 500,
    "xmv_1": 500,
    "xmv_2": 500,
    "xmv_3": 500,
    "xmv_4": 500,
    "xmv_5": 500,
    "xmv_6": 500,
    "xmv_7": 500,
    "xmv_8": 500,
    "xmv_9": 500,
    "xmv_10": 500,
    "xmv_11": 500
}

# Send the POST request with the data
response = requests.post(url, json=data)

# Parse the JSON response
result = response.json()

# Print the prediction
print('Prediction:', result['prediction'])
