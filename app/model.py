from db import *
import flask
import json
from __init__ import jsonrpc
from __init__ import app,db
from werkzeug.contrib.cache import MemcachedCache
import sys
from db_struct import *


cache = MemcachedCache(['127.0.0.1:11211'])

# app = flask.Flask(__name__)

def get_user_by_nick(nick):
	return query_all("""
    SELECT * FROM "User"
    WHERE "nick" LIKE %(nick)s;
        """, nick = str(nick))

def get_participants_of_chat(chat_id):
	return query_all("""
		SELECT "Chat".chat_id,"Chat".name AS "person1","User".name AS "person2" 
		FROM "Chat","User"
		WHERE "chat_id" = {} 
		AND "Chat".user_id = "User".user_id""".format(chat_id))

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
	chats = cache.get('user_chats_{}'.format(user_id))
	if chats is None:
		chats = (query_all("""
				SELECT * FROM "Chat"
				WHERE "user_id" = {};
				""".format(user_id)))
		cache.set('user_chats_{}'.format(user_id),chats,timeout=10*60)
		print("put in cache:",chats,file=sys.stdout)
		return (flask.jsonify(chats))
	else:
		print("taken from cache:",chats,file=sys.stdout)
		return (flask.jsonify(chats))

@jsonrpc.method('get_messages')
def get_messages(chat_id):
	return json.dumps(query_all("""
	SELECT * FROM "Message"
	WHERE "chat_id" = %(chat_id)s;
	""",
	chat_id = int(chat_id)),indent=4, sort_keys=True, default=str)

@jsonrpc.method('get_users')
def get_users():
	return json.dumps(query_all("""
	SELECT * FROM "User"
	"""),indent=4, sort_keys=True, default=str)

@jsonrpc.method('add_new_chat')
def add_new_chat(is_group_chat,name,unread,key,avatar,user_id):
	add_value(Chat(is_group_chat=is_group_chat,name = name,unread = unread,key = key,avatar= avatar,user_id = user_id))
	commit_value()

@jsonrpc.method('add_new_user')
def add_new_user(name,nick,avatar):
	add_value(User(name=name,nick=nick,avatar=avatar))
	commit_value()


@jsonrpc.method('add_new_message')
def add_new_message(content,sent,chat_id):
	add_value(content=content,sent=sent,chat_id=chat_id)
	commit_value()

@jsonrpc.method('add_new_attach')
def add_new_attach(type,size,chat_id):
	add_value(type=type,size=size,chat_id=chat_id)
	commit_value()





