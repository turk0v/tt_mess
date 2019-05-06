from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from __init__ import db,app
from db_struct import Chat,User,Message,Attachment
from db import add_value,commit_value
from model import add_new_user
add_new_user(name="name3",nick="nick4",avatar=None)
chat1 = Chat(is_group_chat = True,name = "name1",unread = 2,key = 66,avatar= None,user_id = 1)
add_value(chat1)
db.session.add(chat1)
db.session.commit()
# user2 = User(name="name3",nick="nick3",avatar=None)
# add_value(user2)
# commit_value()
# user3 = User(name="name4",nick="nick4",avatar=None,chat_id = 1)
# chat1 = Chat(is_group_chat = True,name = "name1",unread = 2,key = 66,avatar= None,user_id=1,message_id=1)
# user = Chat.query.first()
# print(user.user_chat)
# db.session.add(user3)
# db.session.commit()
# db.metadata.clear()
# db.drop_all()
# db.create_all()