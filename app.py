# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():

    # Return the response in json format
    return jsonify(  {'id': 0,
     'Raw_Sensor_Value': '{} '.format(70),
     'Voltage (mV)': '{}'.format(123),            
     'Current (A)': '{} '.format(67),
     
     })



# A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
