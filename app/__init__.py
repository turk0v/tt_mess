from flask import Flask
import sys
from flask_jsonrpc import JSONRPC
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
import config
from flask_cors import CORS
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from celery_setup import make_celery
from flask_mail import Mail



app = Flask(__name__)
app.config.from_object(config.ProductionConfig)
CORS(app)
jsonrpc = JSONRPC(app,'/api')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{url}:{port}/{db_name}'\
    .format(username=config.DB_USER, password=config.DB_PASS, url=config.DB_HOST,
            port=config.DB_PORT, db_name=config.DB_NAME)


db = SQLAlchemy(app)
app.config.update(
	broker_url='redis://localhost:6379',
	result_backend='redis://localhost:6379',
	include=['celery_tasks']
	)
app.config.update(
	MAIL_SERVER = 'smtp.googlemail.com',
	MAIL_PORT = 465,
	MAIL_USERNAME = config.MAIL_USERNAME,
	MAIL_PASSWORD = config.MAIL_PASSWORD,
	MAIL_USE_SSL = True,
	MAIL_USE_TLS = False,
	ADMINS = ['bigmat1999@gmail.com']
	)

celery = make_celery(app)
mail = Mail(app)


migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
# app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
