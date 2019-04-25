from app import db

class User(db.Model):

	__tablename__ = 'User'
	id = db.Column('id',db.Integer,primary_key = True)
	name = db.Column("name",db.String(100),nullable=False)
	nick = db.Column("nick",db.String(100),nullable=False,unique = True)
	avatar = db.Column("avatar",db.String(100),default = None)
	email = db.Column("email",db.String(100),unique = True)
	# chat_user = db.relationship('Chat', back_populates = 'user_chat')

	def __repr__(self):
		return f"User('{self.name}','{self.nick}','{self.avatar}','{self.email}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
	def get_id(self):
		return self.id