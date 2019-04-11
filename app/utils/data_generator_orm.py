import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
from db_methods import *
from model import add_new_user,add_new_message,add_new_chat
import pandas as pd
from random import randint,choice
import flask
from __init__ import jsonrpc
from __init__ import app
from db_struct import *


users_nick = {'Jack':'jack237','Sam':'helo2','Glen':'username','Todd':'123456qwerty','Fred':'frog'}
messages = ['hi','whats up','sup','how are you','fine','thnx','bye','ok','asap','sorry','acab','lmao','super','lol','not funny'
			,'strange','good morning','see you','U fine?','4fun','jk','i h8 u','so do i','hahahahaha','stupid','i love it']

def time_formater():
	rand_time_add_hour = randint(1,2)
	rand_time_add_minute = randint(1,2)
	rand_time_add_second = randint(1,2)
	rand_time_add_month = randint(1,3)
	return ("{}-{}-{} {}:{}:{}".format(
		pd.datetime.now().year,pd.datetime.now().month,pd.datetime.now().day+rand_time_add_month,
		pd.datetime.now().hour + rand_time_add_hour,pd.datetime.now().minute+rand_time_add_minute ,pd.datetime.now().second+rand_time_add_second))

def rand_person(object_in,user):
	if (type(object_in) == dict):
		tmp = dict(object_in)
		tmp.pop(user)
	else:
		tmp = list(object_in)
		tmp.remove(user)
	tmp_keys = []
	for key in tmp:
		tmp_keys.append(key)
	return(tmp_keys)

def add_messages(number_to_gen,chat_id) :
	for i in range(0,number_to_gen-1):
		add_new_message(str(choice(messages)),time_formater(),chat_id)
		print(f"added message to {chat_id}")

def get_id_user(filter):
	res = User.query.filter_by(nick=filter).first()
	return(res.get_id())

def get_id_chat(filter):
	res = Chat.query.filter_by(user_id=filter).first()
	return(res.get_id())

with app.app_context():
	for user in users_nick :
		# chat_id1_gen = randint(5010,7500)
		chat_id2_gen = randint(7510,10000)
		message_id1_gen = randint(10010,25000)
		message_id2_gen = randint(25010,50000)
		add_new_user(user,users_nick[user],None,f'example{chat_id2_gen}@gmail.com')
		print("added user with name {}".format(user))
		tmp = rand_person(users_nick,user)
		adding_user = str(choice(tmp))
		user_id_gen = get_id_user(users_nick[user])
		add_new_chat(False,adding_user,0,randint(0,10000),None,user_id_gen)
		add_new_chat
		print(f"added chat {adding_user} with {users_nick[user]}")
		chat_id1_gen = get_id_chat(user_id_gen)
		add_messages(10,chat_id1_gen)
		tmp = rand_person(tmp,adding_user)
		add_new_chat(False,str(choice(tmp)),0,randint(0,10000),None,user_id_gen)
		chat_id2_gen = get_id_chat(user_id_gen)
		add_messages(10,chat_id2_gen)





