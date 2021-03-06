from __init__ import celery
import sys
from app.utils import send_mail
sys.path.insert(0, '/Users/matveyturkov/tt_mess/instance/')
from send_mail import send_mail
from secret import MAIL_USERNAME
from celery.decorators import periodic_task
from datetime import timedelta
@celery.task()
def send_mail_on_chat(name,chat_with,email):
	message_to_send = f"{name}, you got new chat with {chat_with}"
	theme_to_send = "Chat created"
	send_mail(MAIL_USERNAME,email,theme_to_send,message_to_send,f"{message_to_send}")


@celery.task()
def send_mail_periodic():
	email = "turkov.mm@phystech.edu"
	message_to_send = f"Hey {email}, it is your periodic mail"
	theme_to_send = "Periodic"
	print(message_to_send)
	send_mail(MAIL_USERNAME,email,theme_to_send,message_to_send,f"{message_to_send}")

