from __init__ import db
from flask_sqlalchemy import SQLAlchemy
import datetime

class Member(db.Model):
    __tablename__ = 'Member'
    id = db.Column('id',db.Integer,primary_key = True)
    user_id = db.Column('user_id',db.Integer, db.ForeignKey('User.id', ondelete='cascade'),nullable=False)
    chat_id = db.Column('chat_id',db.Integer, db.ForeignKey('Chat.id', ondelete='cascade'),nullable=False)
    last_unread_message_id = db.Column('last_unread_message_id',db.Integer,db.ForeignKey('Message.id', ondelete='cascade'),nullable=False)


class Attachment(db.Model):
	__tablename__ = 'Attachment'
	id = db.Column('id',db.Integer,primary_key = True)
	user = db.relationship('User', backref = 'attachment')
	chat = db.relationship('Chat', backref = 'attachment')
	message = db.relationship('Message', backref = 'attachment')
	a_type = db.Column("type",db.String(20),nullable=False)
	size = db.Column("size",db.Integer,nullable=False)



class Chat(db.Model):
	__tablename__ = 'Chat'
	id = db.Column('id',db.Integer,primary_key = True)
	is_group_chat = db.Column('is_group_chat',db.Boolean,nullable=True)
	name = db.Column("name",db.String(100),nullable=False)
	unread = db.Column("unread",db.Integer)
	key = db.Column("key",db.Integer,unique=True)
	avatar = db.Column("avatar",db.String(100),default = None)
	user = db.relationship('User', backref = 'chat')
	message = db.relationship('Message', backref = 'chat')



class User(db.Model):
	__tablename__ = 'User'
	id = db.Column('id',db.Integer,primary_key = True)
	name = db.Column("name",db.String(100),nullable=False)
	nick = db.Column("nick",db.String(100),nullable=False,unique = True)
	avatar = db.Column("avatar",db.String(100),default = None)
	chat = db.relationship('Chat', backref = 'user')
	message = db.relationship('Message', backref = 'user')



class Message(db.Model):
	__tablename__ = 'Message'
	id = db.Column('id',db.Integer,primary_key = True)
	content = db.Column("content",db.String(500),nullable = False)
	sent = db.Column("sent",db.DateTime,nullable = False,default = datetime.datetime.now)
	user = db.relationship('User', backref = 'message')
	chat = db.relationship('Chat', backref = 'message')



