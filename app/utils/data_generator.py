import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/')
from db import *
from model import add_new_user,add_new_message,add_new_chat
import postgresql
import pandas as pd
from random import randint,choice
import flask
from __init__ import jsonrpc
app = flask.Flask(__name__)


users_nick = {'Jack':'jack237','Sam':'helo2','Glen':'username','Todd':'123456qwerty','Fred':'frog'}
messages = ['hi','whats up','sup','how are you','fine','thnx','bye','ok','asap','sorry','acab','lmao','super','lol','not funny'
			,'strange','good morning','see you','U fine?','4fun','jk','i h8 u','so do i','hahahahaha','stupid','i love it']

def time_formater():
	rand_time_add_hour = randint(1,2)
	rand_time_add_minute = randint(1,2)
	rand_time_add_second = randint(1,10)
	rand_time_add_month = randint(1,5)
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

def add_messages(number_to_gen,last_message_id,chat_id,user_id) :
	for i in range(0,number_to_gen-1):
		message_id_gen = randint(50001,120000)
		add_new_message(message_id_gen,chat_id,user_id,str(choice(messages)),time_formater())
		print("added message with id {}".format(message_id_gen))
	add_new_message(last_message_id,chat_id,user_id,str(choice(messages)),time_formater())
	print("added last message with id {}".format(last_message_id))


# with app.app_context():
	for user in users_nick :
		user_id_gen = randint(100,5000)
		chat_id1_gen = randint(5010,7500)
		chat_id2_gen = randint(7510,10000)
		message_id1_gen = randint(10010,25000)
		message_id2_gen = randint(25010,50000)
		key_gen = randint(0,99)
		add_new_user(user_id_gen,user,users_nick[user],None)
		print("added user with id {}".format(user_id_gen))
		tmp = rand_person(users_nick,user)
		adding_user = str(choice(tmp))
		add_new_chat(chat_id1_gen,False,message_id1_gen,adding_user,0,key_gen,None,user_id_gen)
		print("added chat with id {}".format(chat_id1_gen))
		add_messages(10,message_id1_gen,chat_id1_gen,user_id_gen)
		tmp = rand_person(tmp,adding_user)
		add_new_chat(chat_id2_gen,False,message_id2_gen,str(choice(tmp)),0,key_gen,None,user_id_gen)
		print("added chat with id {}".format(chat_id2_gen))
		add_messages(10,message_id2_gen,chat_id2_gen,user_id_gen)



