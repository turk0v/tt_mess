import datetime
import json
import flask
from model import get_chats
from flask_cors import CORS
from __init__ import app
from model import get_participants_of_chat
with app.app_context():
	print(type(get_participants_of_chat(6765)))
	# print((get_messages(6765)))
	# print(jsonify(get_chats(4665)))