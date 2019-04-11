from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm
from wtforms import StringField, validators
from db_struct import User
from wtforms import Form, BooleanField, StringField, PasswordField, validators
 
class UserForm(ModelForm):
	name = StringField('name', default='Unnamed')
	nick = StringField('nick', [validators.Length(min=5)])
	avatar = StringField('avatar', [validators.Optional()], default='')