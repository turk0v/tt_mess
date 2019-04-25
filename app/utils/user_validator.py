from wtforms_alchemy import ModelForm
from wtforms import StringField, validators
from wtforms.fields.html5 import EmailField


class UserForm(ModelForm):
	name = StringField('name', default='Unnamed')
	nick = StringField('nick', [validators.Length(min=5)])
	avatar = StringField('avatar', [validators.Optional()], default='')
	email = EmailField('email',[validators.DataRequired(), validators.Email()])