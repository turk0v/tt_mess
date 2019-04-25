from app import db
from app.models.user import User


def get_email(user_id):
	return User.query.filter_by(id = user_id).first().email

def get_name(user_id):
	return User.query.filter_by(id = user_id).first().name