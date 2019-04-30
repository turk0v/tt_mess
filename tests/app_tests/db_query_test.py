import unittest
import sys
import requests
sys.path.insert(0,'/Users/matveyturkov/tt_mess')
from app import get_chats,app,validate_user,User,add_new_message,get_message,remove_message


class DbQueryTest(unittest.TestCase):
	def test_get_chats(self):
		chat_list = [	{'id': '1', 'is_group_chat': 'False', 'name': 'Todd', 
						'unread': '0', 'key': '1750', 'avatar': 'None', 'user_id': '1'}, 
						{'id': '2', 'is_group_chat': 'False', 'name': 'Fred', 
						'unread': '0', 'key': '1625', 'avatar': 'None', 'user_id': '1'}]
		with app.app_context():
			self.assertTrue(get_chats(1),chat_list)

	def test_request(self):
		user_list = [	{"avatar":"None","email":"example8669@gmail.com","id":"1","name":"Jack","nick":"jack237"},
						{"avatar":"None","email":"example8191@gmail.com","id":"2","name":"Sam","nick":"helo2"},
						{"avatar":"None","email":"example9206@gmail.com","id":"3","name":"Glen","nick":"username"},
						{"avatar":"None","email":"example8545@gmail.com","id":"4","name":"Todd","nick":"123456qwerty"},
						{"avatar":"None","email":"example8347@gmail.com","id":"5","name":"Fred","nick":"frog"},
						{"avatar":"None","email":"turkoov@gmail.com","id":"6","name":"Matt","nick":"matt128"}]
		url = 'http://127.0.0.1:5002/get_users'
		req = requests.get(url).text
		self.assertTrue(req,user_list)

	def test_validator(self):
		short_nick = User(name='u', nick='u1', avatar='', email = '@.com')
		self.assertFalse(validate_user(short_nick))

	def test_index_page(self):
		url = 'https://turkovmatvei.chickenkiller.com/'
		res = requests.get(url)
		self.assertTrue(res.text,'<h1 style=\'color:blue\'>Hello There!</h1>')

	def test_add_and_delete_message(self):
		message = {"content": "test_message","sent":"2019-04-15 01:46:07","chat_id":1}
		with app.app_context():
			mess_id = add_new_message(message["content"],message['sent'],message["chat_id"])
			res = get_message(mess_id)
			self.assertTrue(message,res)
			res = remove_message(mess_id)
			self.assertTrue(res,True)





if __name__ == "__main__":
	unittest.main()
