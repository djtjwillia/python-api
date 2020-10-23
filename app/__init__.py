import flask
from flask import request, jsonify
from datetime import datetime
#from . import config

#flask setup
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#api setup, putting our hardcoded message here.
message = 'Automate all the things!'
return_dict = {}

def create_app(config_name):
    #app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')
    return app

#setting up a default page, itll be ugly but meh
@app.route('/', methods=['GET'])
def home():
    return "<h1>Demo API</h1><p>This site is a demo API.</p>"

#setting the api/v1/message route to return our message
@app.route('/api/v1/message/', methods=['GET'])
def api_base():
    #grab the time
    timestamp = datetime.now().strftime("%s")
    #build the return as a dictionary, setting time to be posix style
    for var in ["message", "timestamp"]:
        return_dict[var] = eval(var)
    return jsonify(return_dict)






def test_home():
    with app.test_client() as client:
        response = client.get('/')
        data = json.loads(resp.data)
        assert b'This site is a demo API' in response.data



def test_api_base():
    with app.test_client() as client:
        response = client.get('/api/v1/message/')
        data = json.loads(resp.data)
        assert b'Automate all the things!' in response.data