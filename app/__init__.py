from flask import Flask
import sys
from flask_jsonrpc import JSONRPC
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
import config
from flask_cors import CORS
import datetime
# from werkzeug.contrib.profiler import ProfilerMiddleware

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object(config.ProductionConfig)
CORS(app)
jsonrpc = JSONRPC(app,'/api')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{url}:{port}/{db_name}'\
    .format(username=config.DB_USER, password=config.DB_PASS, url=config.DB_HOST,
            port=config.DB_PORT, db_name=config.DB_NAME)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
# app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
@app.route('/')
def index():
    return "Hello, World!"

from model import *
if __name__ == '__main__':
    app.run(debug=True)