import flask
from flask import request, jsonify
import random
import time
import random




app = flask.Flask(__name__)
app.config["DEBUG"] = True


def update():
    import time
    while True:
        x = random.random()
        time.sleep(5)
        return x

# Create some test data for our catalog in the form of a list of dictionaries.




# A route to return all of the available entries in our catalog.
@app.route('/sadsdsd', methods=['GET'])
def api_all():
    return jsonify(
        {'id': 0,
     'Current_generated': '{} Amperes'.format(123),
     'Current_consumed': '{} Amperes'.format(67),
     
     }
     )

app.run(debug=True, port=33507)
