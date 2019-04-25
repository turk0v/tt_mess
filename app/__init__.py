from flask import Flask,jsonify
import sys
from flask_jsonrpc import JSONRPC
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from celery_setup import make_celery
from flask_mail import Mail




app = Flask(__name__)
app.config.from_object(config.ProductionConfig)
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




if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1', port= 5002)

