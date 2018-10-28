from db import *
import flask

app = flask.Flask(__name__)

def get_user(name):
	return query_all("""
    SELECT * FROM "User"
    WHERE "name" LIKE %(name)s;
        """, name = str(name))


def get_chats():
	return query_all("""
	SELECT * FROM "Chat";
	""")

def add_new_chat(chat_id,is_group_chat,topic,last_message):
	execute("""
	INSERT INTO "Chat" VALUES(%(chat_id)s, %(is_group_chat)s, %(topic)s, %(last_message)s);
	""",
	chat_id = int(chat_id),
	is_group_chat = 'true' if is_group_chat else 'false',
	topic = str(topic),
	last_message = int(last_message))
	commit()
