from __init__ import db
from flask_sqlalchemy import SQLAlchemy
import datetime


class Attachment(db.Model):
	__tablename__ = 'Attachment'
	id = db.Column('id',db.Integer,primary_key = True)
	a_type = db.Column("type",db.String(20),nullable=False)
	size = db.Column("size",db.Integer,nullable=False)
	attach_chat_id = db.Column('chat_id',db.Integer, db.ForeignKey('Chat.id'))
	# chat_attachment = db.relationship('Chat', back_populates = 'attachment_chat')

	def __repr__(self):
		return f"Chat('{self.is_group_chat}','{self.name}','{self.unread}','{self.key}','{self.avatar}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Chat(db.Model):
	__tablename__ = 'Chat'
	id = db.Column('id',db.Integer,primary_key = True)
	is_group_chat = db.Column('is_group_chat',db.Boolean,nullable=True)
	name = db.Column("name",db.String(100),nullable=False)
	unread = db.Column("unread",db.Integer)
	key = db.Column("key",db.Integer,unique=True)
	avatar = db.Column("avatar",db.String(100),default = None)
	user_id = db.Column('user_id',db.Integer, db.ForeignKey('User.id'))

	# message_chat = db.relationship('Message', back_populates = 'chat_message')
	# attachment_chat = db.relationship('Attachment', back_populates = 'chat_attachment')


	def __repr__(self):
		return f"Chat('{self.is_group_chat}','{self.name}','{self.unread}','{self.key}','{self.avatar}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class User(db.Model):
	__tablename__ = 'User'
	id = db.Column('id',db.Integer,primary_key = True)
	name = db.Column("name",db.String(100),nullable=False)
	nick = db.Column("nick",db.String(100),nullable=False,unique = True)
	avatar = db.Column("avatar",db.String(100),default = None)
	# chat_user = db.relationship('Chat', back_populates = 'user_chat')

	def __repr__(self):
		return f"User('{self.name}','{self.nick}','{self.avatar}','{self.chat_id}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}



class Message(db.Model):
	__tablename__ = 'Message'
	id = db.Column('id',db.Integer,primary_key = True)
	content = db.Column("content",db.String(500),nullable = False)
	sent = db.Column("sent",db.DateTime,nullable = False,default = datetime.datetime.now)
	mess_chat_id = db.Column('chat_id',db.Integer, db.ForeignKey('Chat.id'))
	# chat_message = db.relationship('Chat', backref = 'message_chat')

	def __repr__(self):
		return f"Chat('{self.is_group_chat}','{self.name}','{self.unread}','{self.key}','{self.avatar}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}