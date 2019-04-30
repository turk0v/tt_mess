import sys
DEV_PATH = '/Users/matveyturkov/tt_mess/instance/'
PROD_PATH = '/home/ubuntu/tt_mess/instance'
sys.path.insert(0, DEV_PATH)
from secret import DB_USER,DB_PASS,DB_HOST,DB_PORT,DB_NAME,DB_SERVER_HOST,DB_SERVER_PASSWORD,MAIL_USERNAME as mail_user,MAIL_PASSWORD as mail_pass
from flask import Config
import datetime

class DevelopmentConfig(Config):
	ENV = 'development'
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{url}:{port}/{db_name}'\
	    .format(username=DB_USER, password=DB_PASS, url=DB_HOST,
	            port=DB_PORT, db_name=DB_NAME)
	BROKER_URL='redis://localhost:637'
	RESULT_BACKEND='redis://localhost:6379'
	INCLUDE=['celery_tasks']
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = mail_user
	MAIL_PASSWORD = mail_pass
	MAIL_USE_SSL = True
	MAIL_USE_TLS = False
	ADMINS = ['bigmat1999@gmail.com']
	PATH_MAIN = '/Users/matveyturkov/tt_mess/'

class ProductionConfig(Config):
	ENV = 'production'
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{url}/{db_name}'\
	    .format(username=DB_USER, password=DB_SERVER_PASSWORD, url=DB_SERVER_HOST, db_name=DB_NAME)
	BROKER_URL='redis://localhost:6379'
	RESULT_BACKEND='redis://localhost:6379'
	INCLUDE=['celery_tasks']
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = mail_user
	MAIL_PASSWORD = mail_pass
	MAIL_USE_SSL = True
	MAIL_USE_TLS = False
	ADMINS = ['bigmat1999@gmail.com']
	PATH_MAIN = '/home/ubuntu/tt_mess/'




		