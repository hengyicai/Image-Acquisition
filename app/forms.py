# -*- encoding: utf-8 -*-

from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from flask.ext.wtf import Required


class ExampleForm(Form):
    title = TextField(u'Título', validators=[Required()])
    content = TextAreaField(u'Conteúdo')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')


# recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
    user = TextField(u'Username', validators=[Required()])
    password = PasswordField(u'Password', validators=[Required()])
