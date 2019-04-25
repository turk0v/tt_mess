from app import db

class Attachment(db.Model):
	__tablename__ = 'Attachment'
	id = db.Column('id',db.Integer,primary_key = True)
	a_type = db.Column("type",db.String(20),nullable=False)
	size = db.Column("size",db.Integer,nullable=False)
	attach_chat_id = db.Column('chat_id',db.Integer, db.ForeignKey('Chat.id'))

	def __repr__(self):
		return f"Attachment('{self.a_type}','{self.size}','{self.attach_chat_id}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
	def get_id(self):
		return self.id