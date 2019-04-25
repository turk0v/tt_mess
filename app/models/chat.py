from app import db

class Chat(db.Model):
	__tablename__ = 'Chat'
	id = db.Column('id',db.Integer,primary_key = True)
	is_group_chat = db.Column('is_group_chat',db.Boolean,nullable=True)
	name = db.Column("name",db.String(100),nullable=False)
	unread = db.Column("unread",db.Integer)
	key = db.Column("key",db.Integer,unique=True)
	avatar = db.Column("avatar",db.String(100),default = None)
	user_id = db.Column('user_id',db.Integer, db.ForeignKey('User.id'))


	def __repr__(self):
		return f"Chat('{self.is_group_chat}','{self.name}','{self.unread}','{self.key}','{self.avatar}')"
	def as_dict(self):
		return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
	def get_id(self):
		return self.id