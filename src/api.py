import flask
from flask import request, jsonify
from datetime import datetime

#flask setup
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#api setup, putting our hardcoded message here.
message: 'Automate all the things!'
return_dict = {}

#setting up a default page, itll be ugly but meh
@app.route('/', methods=['GET'])
def home():
    return "<h1>Demo API</h1><p>This site is a demo API.</p>"

#setting the api/v1/message route to return our message
@app.route('/api/v1/message/' methods=['GET'])
def api_base():
    #grab the time
    timestamp = datetime.now().strftime("%s")
    #build the return as a dictionary, setting time to be posix style
    for var in ["message", "timestamp"]:
        return_dict[var] = eval(var)
    return jsonify(return_dict)

app.run()