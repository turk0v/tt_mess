from flask import request, abort ,jsonify,render_template
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app')
from __init__ import app,jsonrpc
from fake_json_data import * 
from model import *
import json
# @app.route('/')
# def index(name = "World"):
# 	return render_template("home.html",name = 'bio')
# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response




# /search_users/
# /search_chats/
# /list_chats/
# /create_pers_chat/
# /create_group_chat/
# /add_members_to_group_chat/
# /leave_group_chat/
# /send_message/
# /read_message/
# /upload_file/