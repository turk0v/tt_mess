from flask import request, abort ,jsonify,render_template
from app import app

CHATS_LIST = ['tmp1','tmp2','tmp3']
CONTACTS_LIST = ['Profile1', 'Profile2', 'Profile3']


@app.route('/<string:name>/')
@app.route('/')
def index(name = "World"):
	return render_template("home.html",name = name)


@app.route('/form/', methods = ['POST', 'GET'])
def form():
	if request.method == 'GET':
		return render_template("form.html")
	else:
		return_value = jsonify(request.form)
		return return_value

@app.route('/chats/', methods = ['GET'])
def get_chats_list():
	result = {}
	result['status_code'] = '200 OK'
	result['mimetype'] = 'application/json'
	result['chats'] = CHATS_LIST
	return jsonify(result)

@app.route('/contacts/', methods = ['GET'])
def get_contacts_list():
	result = {}
	result['status_code'] = '200 OK'
	result['mimetype'] = 'application/json'
	result['contacts'] = CONTACTS_LIST
	return jsonify(result)


@app.route('/new_chat/', methods = ['GET', 'POST'])
def create_new_chat():
	if request.method == 'GET':
		return render_template("new_chat.html")
	else:
		CHATS_LIST.append(request.form['chat_name'])
		return jsonify(request.form)