import unittest
from app import app
from flask import jsonify

class ExpectedFailureTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_wrong_method(self):
    	rv = self.app.post('/chats/')
    	self.assertEqual(rv.data,'broken')

class FlaskTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_index(self):
		return_value = self.app.get('/')
		self.assertEqual(200, return_value.status_code)
		self.assertEqual(b'<h2>Hello,World</h2>', return_value.data)
		self.assertEqual('text/html', return_value.mimetype)

	def test_form(self):
		rv = self.app.post('/form/', data = {'first_name': "first", 'last_name': 'last'})
		self.assertEqual(b'{"first_name":"first","last_name":"last"}\n', rv.data)

	def test_chats(self):
		rv = self.app.get('/chats/')
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(200, rv.status_code)
		self.assertEqual(b'{"chats":["tmp1","tmp2","tmp3"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)

	def test_contacts(self):
		rv = self.app.get('/contacts/')
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(200, rv.status_code)
		self.assertEqual(b'{"contacts":["Profile1","Profile2","Profile3"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)

	def test_new_chat(self):
		rv = self.app.post('/new_chat/', data = {"chat_name": "test"})
		self.assertEqual(200, rv.status_code)
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(b'{"chat_name":"test"}\n', rv.data)


if __name__ == "__main__":
	unittest.main()



