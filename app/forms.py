from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app.models.Authors import Authors
from app.models.User import User
from app.models.Tags import Tags


class ArticleForm(FlaskForm):
  author = QuerySelectField('Autorius', query_factory=Authors.query.all, validators=[DataRequired()])
  tags = QuerySelectMultipleField('Žymos', query_factory=Tags.query.all)
  date = DateField('Data', [DataRequired()])
  title = StringField('Pavadinimas', [DataRequired(), Length(min=10)])
  text = TextAreaField('Tekstas', [DataRequired(), Length(min=50)])


class RegistrationForm(FlaskForm):
  email = StringField('El. paštas', [DataRequired(), Email()])
  password = PasswordField('Slaptažodis', [DataRequired()])
  confirm_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])

  def check_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class LoginForm(FlaskForm):
  email = StringField('El. paštas', [DataRequired(), Email()])
  password = PasswordField('Slaptažodis', [DataRequired()])
  remember = BooleanField('Prisiminti')


class UserProfileEditForm(FlaskForm):
    email = StringField('El. paštas', [DataRequired(), Email()])
    picture = FileField('Atnaujinti profilio nuotrauką', validators=[FileAllowed(['jpg', 'png'])])

    def check_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(el_pastas=email.data).first()
            if user:
                raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class UserRequestResetPasswordForm(FlaskForm):
    email = StringField('El. paštas', [DataRequired(), Email()])


class UserResetPasswordForm(FlaskForm):
    password = PasswordField('Slaptažodis', [DataRequired()])
    confirm_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])
