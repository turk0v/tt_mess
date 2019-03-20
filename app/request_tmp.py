from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from __init__ import db,app
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)