from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/introduction/', methods=['GET'])
def home():
    return "<h1>BAM!</h1><p>This is straight my own API, sirrrrr.</p>"


@app.route('/puppies/', methods=['GET'])
def house():
    return "<h1>BAM!</h1><p>This is straight my own puppy, sirrrrr.</p>"

@app.route('/add/', methods=['POST'])
def add():
    num1 = int(request.form["first_num"])
    num2 = int(request.form["second_num"])
    return str(num1 + num2)
app.run()
