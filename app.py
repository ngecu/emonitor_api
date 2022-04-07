# app.py
import random
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    data=[]
    for n in range(11):
        data.append({"id":n,
                     'Raw_Sensor_Value': '{} '.format(random.randint(500, 550)),
                      'Voltage_(mV)': '{}'.format(random.randint(155, 389)/1000),            
                       'Current_(A)': '{} '.format(random.randint(-155, 389)/1000),})
    
    # Return the response in json format
    return jsonify(data)



# A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
