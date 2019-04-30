from app import app,jsonrpc
from app.api.api_methods import add_value,delete_value,commit_value
from app.models.db_methods import get_email,get_name
from app.models.user import User
from app.models.chat import Chat
from app.models.message import Message
from app.models.attachment  import Attachment
import flask
from app.utils.user_validator import UserForm


@app.errorhandler(404)
def not_found(error):
    return (flask.jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def not_found(error):
    return (flask.jsonify({'error': 'Wrong method'}), 405)

@app.route("/")
def hello():
	return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/get_users/',methods=['GET'])
def get_users():
	response =  []
	for user in (User.query.all()):
		response.append(user.as_dict())
	return flask.jsonify(response)

@app.route('/get_chats/<user_id>',methods=['GET'])
def get_chats(user_id):
	chats = []
	for chat in (Chat.query.filter_by(user_id = user_id)):
		chats.append(chat.as_dict())
	return flask.jsonify(chats)

def validate_user(user):
	return UserForm(None, user).validate()


@app.route('/get_messages/<chat_id>',methods=['GET'])
def get_messages(chat_id):
	response = []
	for message in (Message.query.filter_by(chat_id = chat_id)):
		response.append(message.as_dict())
	return flask.jsonify(response)

@app.route('/get_message/<message_id>',methods=['GET'])
def get_message(message_id):
	response = []
	for message in (Message.query.filter_by(id = message_id)):
		response.append(message.as_dict())
	return flask.jsonify(response)

@app.route('/get_user/<user_id>',methods=['GET'])
def get_user(user_id):
	response = []
	for user in (User.query.filter_by(id = user_id)):
		response.append(user.as_dict())
	return flask.jsonify(response)


@jsonrpc.method('add_new_chat')
def add_new_chat(is_group_chat,name,unread,key,avatar,user_id):
	add_value(Chat(is_group_chat=is_group_chat,name = name,unread = unread,key = key,avatar= avatar,user_id = user_id))
	commit_value()
	email = get_email(user_id)
	name_chat_got = get_name(user_id)
	send_mail_on_chat.delay(name_chat_got,name,email)


@jsonrpc.method('add_new_user')
def add_new_user(name,nick,avatar,email):
	user = User(name=name,nick=nick,avatar=avatar,email = email)
	add_value(user)
	commit_value()
	return(user.id)


@jsonrpc.method('add_new_message')
def add_new_message(content,sent,chat_id):
	message = Message(content=content,sent=sent,chat_id=chat_id)
	add_value( message )
	commit_value()
	return (message.id)

@jsonrpc.method('add_new_attach')
def add_new_attach(type,size,chat_id):
	add_value(Attachment(type=type,size=size,chat_id=chat_id))
	commit_value()


@jsonrpc.method('remove_message')
def remove_message(message_id):
	delete_value(Message.query.filter_by(id = message_id).first())
	commit_value()
	return(True)


@jsonrpc.method('remove_user')
def remove_user(user_id):
	delete_value(User.query.filter_by(id = user_id).first())
	commit_value()
	return(True)



@jsonrpc.method('remove_all_messages')
def remove_all_messages(chat_id):
	for message in Message.query.filter_by(chat_id = chat_id):
		delete_value(message)
		commit_value()

@jsonrpc.method('change_message_content')
def change_message_content(message_id,content):
	message_tmp = Message.query.filter_by(id = message_id).first()
	message_tmp.content = str(content)
	commit_value()






