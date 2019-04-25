from app import db

def add_value(obj):
	db.session.add(obj)

def delete_value(obj):
	db.session.delete(obj)

def commit_value():
	db.session.commit()


