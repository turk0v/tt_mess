import flask
import psycopg2
import psycopg2.extras
from __init__ import db
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
from db_struct import Chat, User

def add_value(obj):
	db.session.add(obj)

def delete_value(obj):
	db.session.delete(obj)

def commit_value():
	db.session.commit()

def get_email(user_id):
	return User.query.filter_by(id = user_id).first().email

def get_name(user_id):
	return User.query.filter_by(id = user_id).first().name


def get_connection():
	if not hasattr(flask.g,'dbconn'):
		flask.g.dbconn = psycopg2.connect(user='matveyturkov',database='mess')
	return flask.g.dbconn

def get_cursor():
	return get_connection().cursor(cursor_factory = psycopg2.extras.DictCursor)

def execute(sql,**params):
	with get_cursor() as cur:
		cur.execute(sql,params)

def query_one(sql, **params):
	with get_cursor() as cur:
		cur.execute(sql,params)
		return dict(cur.fetchone())

def query_all(sql, **params):
	with get_cursor() as cur:
		cur.execute(sql,params)
		result = cur.fetchall()
		return list(map(dict, result))

def commit():
	if hasattr(flask.g,'dbconn'):
		conn = flask.g.dbconn
		conn.commit()
		close()

def rollback():
	if hasattr(flask.g,'dbconn'):
		conn = flask.g.dbconn
		conn.rollback()
		close()

def close():
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.close()
        delattr(flask.g, 'dbconn')
