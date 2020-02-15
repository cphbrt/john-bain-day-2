from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
#CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})


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

@app.route('/happyprime/', methods=['POST'])
def happy():
    num = int(request.form["happy_prime"])
    if is_prime(num):
        if happy_prime(num):
            return str(num) + " is a Happy Prime Number"
        else:
            return str(num) + " is not a Happy Prime Number"
    else:
        return str(num) + " is not a Happy Prime Number"


def happy_prime(input):
    num = 0
    if input == 1:
        return True
    if input == 4:
        return False
    else:
        place = str(input)
        for x in range(0, len(place)):
            num += int(place[x])**2
        return happy_prime(num)


def is_prime(input):
    input = abs(int(input))

    if input < 2:
        return False
    if input % 2 == 0:
        return False
    if not input & 1:
        return False
    for x in range(3, int(input**0.5)+1, 2):
        if input % x == 0:
            return False
    return True
app.run()
