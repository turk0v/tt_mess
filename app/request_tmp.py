import datetime
import json
import flask
from model import get_chats
from flask_cors import CORS
from __init__ import app
from model import get_chats,get_messages
with app.app_context():
	print((get_chats(4665)))
	# print((get_messages(6765)))
	# print(jsonify(get_chats(4665)))