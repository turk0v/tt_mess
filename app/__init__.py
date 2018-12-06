from flask import Flask
import sys
from flask_jsonrpc import JSONRPC
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
from config import DevelopmentConfig,ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)
jsonrpc = JSONRPC(app,'/api/')

from views import *
