import datetime
import json
from model import get_chats
from flask_cors import CORS
from __init__ import app
CORS(app)
with app.app_context():
	x = get_chats()
def wsgi_application(environ, start_response):
	status = '200 OKey'
	headers = [('Content-Type', 'application/json'),('Access-Control-Allow-Origin','http://localhost:3000')]
	body = json.dumps(x)
	start_response(status, headers)
	return [ body.encode('utf-8')]
