import unittest
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app')
import model
import flask
app = flask.Flask(__name__)

with app.app_context():
	class FlaskTest(unittest.TestCase):
		def test_users_list(self):
			self.assertEqual(model.get_user('one'),{0: {'user_id': 1, 'name': 'one', 'nick': 'one', 'avatar': None}})

		def test_add_list_chat(self):
			model.add_new_chat(1,'yes','cats',2)
			model.add_new_chat(2,'','dogs',3)
			self.assertEqual(model.get_chats(),{0: {'chat_id': 1, 'is_group_chat': True, 'topic': 'cats', 'last_message': 2}, 1: {'chat_id': 2, 'is_group_chat': False, 'topic': 'dogs', 'last_message': 3}})

	if __name__ == "__main__":
		unittest.main()