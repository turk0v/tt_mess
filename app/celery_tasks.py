from __init__ import celery
import sys
sys.path.insert(0, '/Users/matveyturkov/tt_mess/app/utils/')
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
from send_mail import send_mail
from config import MAIL_USERNAME
@celery.task()
def send_mail_on_chat(name,chat_with,email):
	message_to_send = f"{name}, you got new chat with {chat_with}"
	theme_to_send = "Chat created"
	print(f"got in celery")
	send_mail(MAIL_USERNAME,email,theme_to_send,message_to_send,f"{message_to_send}")
