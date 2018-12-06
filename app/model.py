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

@jsonrpc.method('get_chats')
def get_chats():
	return query_all("""
	SELECT * FROM "Chat";
	""")

def add_new_chat(chat_id,is_group_chat,last_message,name,unread,key,avatar):
	execute("""
	INSERT INTO "Chat" VALUES(%(chat_id)s, %(is_group_chat)s, %(last_message)s,%(name)s, %(unread)s,%(key)s,%(avatar)s);
	""",
	chat_id = int(chat_id),
	is_group_chat = 'true' if is_group_chat else 'false',
	name = (name),
	last_message = int(last_message),
	unread = int(unread),
	key = int(key),
	avatar=(avatar))
	commit()
with app.app_context():
	print((get_chats()))