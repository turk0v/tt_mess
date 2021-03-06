from flask import Flask,jsonify
import sys
from flask_jsonrpc import JSONRPC
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from app.celery_setup import make_celery
from flask_mail import Mail




app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
jsonrpc = JSONRPC(app,'/api')
celery = make_celery(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

celery.conf.beat_schedule = {
    "30secondsmail": {
        "task": "celery_tasks.send_mail_periodic",
        "schedule": 20.0
    }
}
celery.conf.timezone = 'UTC'


from app.models.user import User
from app.models.chat import Chat
from app.models.message import Message
from app.models.attachment  import Attachment
from app.utils.user_validator import UserForm

from app.api import *


