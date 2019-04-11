from flask_mail import Message
import sys
sys.path.insert(0,'/Users/matveyturkov/tt_mess/app')
from __init__ import app,mail

def send_mail(sender,recipients,theme,body,html):
	message_to_send = Message(
		theme,
		sender = sender,
		recipients = [recipients])
	message_to_send.body = body
	message_to_send.html = html

	with app.app_context():
		mail.connection.send(message_to_send)





