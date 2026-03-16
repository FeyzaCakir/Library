from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
     title =StringField("Kitap Adı", validators=[DataRequired()])
     author= StringField("Yazar",validators=[DataRequired()])
     stock= IntegerField("Stok")
     submit=SubmitField("Kaydet")
     
class RegisterForm(FlaskForm):
     username= StringField("Kullanıcı Adı:", validators=[DataRequired()])
     email= EmailField("Email:", validators=[DataRequired()])
     password= PasswordField("Şifre:", validators=[DataRequired()])
     submit= SubmitField("REGISTER")
     
class LoginForm(FlaskForm):
     email= EmailField("Email:", validators=[DataRequired()])
     password= PasswordField("Şifre:", validators=[DataRequired()])
     submit= SubmitField("LOGIN")