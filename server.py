from flask import Flask
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True

# SERVE WEB PAGES

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def indexHtml():
    return open("static_content/index.html", "r").read()

@app.route('/index.js', methods=['GET'])
def indexJs():
    return open("static_content/index.js", "r").read()

# SERVE API ENDPOINTS

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

# START SERVING

app.run()
