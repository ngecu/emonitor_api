# app.py
import random
from flask import Flask, request, jsonify  
import requests

from requests.exceptions import HTTPError



def get_api():

    url = "https://get.geojs.io/"


    try:
        response = requests.get(url)

    
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 
    else:
        print('Success! gotten your api')
        x = (response.text).split()
        ip_address = x[1]
        print(ip_address)

        return ip_address

        # print(x)


def get_latitude():
    my_api = get_api()
    url = "https://get.geojs.io/v1/ip/geo/{}.json".format(my_api)

    try:
        response = requests.get(url)

    
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 
    else:
        print('Success! gotten your coordinates')
        x = response.json()
        print("Longitude ,",x["longitude"])
        print("Latitude ,",x["latitude"])


        return x
        # x = (response.text).split()
        # ip_address = x[1]
        # print(ip_address)


app = Flask(__name__)

@app.route('/', methods=['GET'])
get_latitude()



# A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)






