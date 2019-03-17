from db import *
import flask
import json
from __init__ import jsonrpc

app = flask.Flask(__name__)

def get_user_by_nick(nick):
	return query_all("""
    SELECT * FROM "User"
    WHERE "nick" LIKE %(nick)s;
        """, nick = str(nick))

def get_user_by_name(name):
	return query_all("""
    SELECT * FROM "User"
    WHERE "name" LIKE %(name)s;
        """, name = str(name))

@jsonrpc.method('get_chats_request')
def get_chats():
	return query_all("""
	SELECT * FROM "Chat";
	""")

@jsonrpc.method('hi',methods=['GET'])
def say_hi():
	response = flask.jsonify({'some': 'data'})
	response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:3000')
	return response

def add_new_chat(chat_id,is_group_chat,last_message,name,unread,key,avatar,user_id):
	execute("""
	INSERT INTO "Chat" VALUES(%(chat_id)s, %(is_group_chat)s, %(last_message)s,%(name)s, %(unread)s,%(key)s,%(avatar)s,%(user_id)s);
	""",
	chat_id = int(chat_id),
	is_group_chat = 'true' if is_group_chat else 'false',
	name = (name),
	last_message = int(last_message),
	unread = int(unread),
	key = int(key),
	avatar=(avatar),
	user_id = int(user_id))
	commit()

def add_new_user(user_id,name,nick,avatar):
	execute("""
	INSERT INTO "User" VALUES(%(user_id)s, %(name)s, %(nick)s, %(avatar)s);
	""",
	user_id = int(user_id),
	name = (name),
	nick = (nick),
	avatar=(avatar))
	commit()

def add_new_message(message_id,chat_id,user_id,content,sent):
	execute("""
	INSERT INTO "Message" VALUES(%(message_id)s, %(chat_id)s, %(user_id)s, %(content)s, %(sent)s);
	""",
	message_id = int(message_id),
	chat_id = int(chat_id),
	user_id = int(user_id),
	content=(content),
	sent = (sent)),
	commit()