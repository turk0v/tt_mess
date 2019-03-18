from flask import Flask
import sys
from flask_jsonrpc import JSONRPC
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
from config import DevelopmentConfig,ProductionConfig
from flask_cors import CORS
#!flask/bin/python


app = Flask(__name__)
app.config.from_object(ProductionConfig)
CORS(app)
jsonrpc = JSONRPC(app,'/api')
@app.route('/')
def index():
    return "Hello, World!"

from model import *
if __name__ == '__main__':
    app.run(debug=True)