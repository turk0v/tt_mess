import unittest
from unittest.mock import patch
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app')
from model import get_participants_of_chat

class MockTest(unittest.TestCase):
	@patch('model.get_participants_of_chat')
	def test_chat_participants(self,mock_models):
		mock_models.get_participants_of_chat.return_value = {
			'chat_id': '6765',
			'person1': 'Todd',
			'person2': 'Jack',
		}

		response = mock_models.get_participants_of_chat()
		self.assertIsNotNone(response)
		self.assertIsInstance(response, dict)

		chat_id = mock_models.get_participants_of_chat(6765)['chat_id']
		person1 = mock_models.get_participants_of_chat(6765)['person1']
		person2 = mock_models.get_participants_of_chat(6765)['person2']

		self.assertEqual(chat_id, '6765')
		self.assertEqual(person1, 'Todd')
		self.assertEqual(person2, 'Jack')
		print('\n')
		print(mock_models.get_participants_of_chat.called)#check called a function or not

if __name__ == "__main__":
    unittest.main()