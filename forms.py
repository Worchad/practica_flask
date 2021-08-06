from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators, HiddenField, PasswordField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')


class LoginForm(Form):
    """docstring for LoginForm."""
    usuario = StringField('Usuario', [
        validators.DataRequired(
            message='El campo de usuario es requerido.'),
    ])
    password = PasswordField(['Contraseña',
        validators.DataRequired(
            message='El campo nombre de contraseña es requerido.'),
        validators.length(
            min=8, message='La contraseña debe poseer mínimo 8 carácteres'),
    ])
    honeypot = HiddenField('', [length_honeypot])
