import unittest
import sys
import requests
PROD_PATH = '/home/ubuntu/tt_mess'
sys.path.insert(0,PROD_PATH)
from app import get_chats,app,validate_user,User,add_new_user,get_user,remove_user


class DbQueryTest(unittest.TestCase):

	def test_validator(self):
		short_nick = User(name='u', nick='u1', avatar='', email = '@.com')
		self.assertFalse(validate_user(short_nick))

	def test_index_page(self):
		url = 'https://turkovmatvei.chickenkiller.com/'
		res = requests.get(url)
		self.assertTrue(res.text,'<h1 style=\'color:blue\'>Hello There!</h1>')

	def test_add_and_delete_user(self):
		user = {"name":"test","nick":"test_nick","avatar":None,"email":"test@gmail.com"}
		with app.app_context():
			user_id = add_new_user(user["name"],user["nick"],user["avatar"],user["email"])
			res = get_user(user_id)
			self.assertTrue(user,res)
			res = remove_user(user_id)
			self.assertTrue(res,True)






if __name__ == "__main__":
	unittest.main()