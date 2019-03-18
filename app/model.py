from db import *
import flask
import json
from __init__ import jsonrpc
from __init__ import app

# app = flask.Flask(__name__)

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

@app.errorhandler(404)
def not_found(error):
    return (flask.jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def not_found(error):
    return (flask.jsonify({'error': 'Wrong method'}), 405)

@jsonrpc.method('get_chats')
def get_chats(user_id):
	return flask.jsonify(query_all("""
	SELECT * FROM "Chat"
	WHERE "user_id" = {};
	""".format(user_id)))

@jsonrpc.method('get_messages')
def get_messages(chat_id):
	return query_all("""
	SELECT * FROM "Messages"
	WHERE "chat_id" = %(chat_id)s;
	""",
	chat_id = int(chat_id))

@jsonrpc.method('add_new_chat')
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

@jsonrpc.method('add_new_user')
def add_new_user(user_id,name,nick,avatar):
	execute("""
	INSERT INTO "User" VALUES(%(user_id)s, %(name)s, %(nick)s, %(avatar)s);
	""",
	user_id = int(user_id),
	name = (name),
	nick = (nick),
	avatar=(avatar))
	commit()

# curl -X POST --data '{"jsonrpc": "2.0", "method": "get_chats", "params": [676], "id": 0}' https://localhost:5000/api

@jsonrpc.method('add_new_message')
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