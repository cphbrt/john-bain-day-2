from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>BAM!</h1><p>This is straight my own API, boiiiiiiii.</p>"

app.run()
