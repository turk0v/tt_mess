import sys
sys.path.insert(0,'/Users/matveyturkov/tt_mess/app')
from model import *
import unittest
from db_struct import User


class FormsTest(unittest.TestCase):

	def test_user_form(self):
		user_good = User(name='user1', nick='nick1', avatar='', email = 'turkoov@gmail.com')
		short_nick = User(name='u', nick='u1', avatar='', email = '@.com')
		self.assertTrue(validate_user(user_good))
		self.assertFalse(validate_user(short_nick))


if __name__ == '__main__':
	unittest.main()