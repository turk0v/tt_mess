import flask
from forms import *
import json
from __init__ import jsonrpc
from __init__ import app,db
import sys
from db_struct import *
import db_methods
from pathlib import Path
import sys
from celery_tasks import send_mail_on_chat

def validate_user(user):
	return UserForm(None, user).validate()

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
	chats = []
	for chat in (Chat.query.filter_by(user_id = user_id)):
		chats.append(chat.as_dict())
	return(chats)


@jsonrpc.method('get_messages')
def get_messages(chat_id):
	response = []
	for message in (Message.query.filter_by(chat_id = chat_id)):
		response.append(message.as_dict())
	return response


@jsonrpc.method('get_users')
def get_users():
	response =  []
	for user in (User.query.all()):
		response.append(user.as_dict())
	return response




@jsonrpc.method('add_new_chat')
def add_new_chat(is_group_chat,name,unread,key,avatar,user_id):
	db_methods.add_value(Chat(is_group_chat=is_group_chat,name = name,unread = unread,key = key,avatar= avatar,user_id = user_id))
	db_methods.commit_value()
	email = db_methods.get_email(user_id)
	name_chat_got = db_methods.get_name(user_id)
	send_mail_on_chat.delay(name_chat_got,name,email)


@jsonrpc.method('add_new_user')
def add_new_user(name,nick,avatar,email):
	db_methods.add_value(User(name=name,nick=nick,avatar=avatar,email = email))
	db_methods.commit_value()


@jsonrpc.method('add_new_message')
def add_new_message(content,sent,chat_id):
	db_methods.add_value( Message(content=content,sent=sent,chat_id=chat_id))
	db_methods.commit_value()

@jsonrpc.method('add_new_attach')
def add_new_attach(type,size,chat_id):
	db_methods.add_value(Attachment(type=type,size=size,chat_id=chat_id))
	db_methods.commit_value()


@jsonrpc.method('remove_message')
def remove_message(message_id):
	db_methods.delete_value(Message.query.filter_by(id = message_id).first())
	db_methods.commit_value()


@jsonrpc.method('remove_all_messages')
def remove_all_messages(chat_id):
	for message in Message.query.filter_by(chat_id = chat_id):
		db_methods.delete_value(message)
		db_methods.commit_value()

@jsonrpc.method('change_message_content')
def change_message_content(message_id,content):
	message_tmp = Message.query.filter_by(id = message_id).first()
	message_tmp.content = str(content)
	db_methods.commit_value()


