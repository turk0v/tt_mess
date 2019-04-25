from app import db
import datetime

class Message(db.Model):
	__tablename__ = 'Message'
	id = db.Column('id',db.Integer,primary_key = True)
	content = db.Column("content",db.String(500),nullable = False)
	sent = db.Column("sent",db.DateTime,nullable = False,default = datetime.datetime.now)
	chat_id = db.Column('chat_id',db.Integer, db.ForeignKey('Chat.id'))

	def __repr__(self):
		return f"Message('{self.content}','{self.sent}','{self.chat_id}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
	def get_id(self):
		return self.id