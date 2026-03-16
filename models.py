from extensions import db #veri tabanı bağlantısı
from flask_login import UserMixin

class Book(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(120),nullable=False)
    author= db.Column(db.String(100),nullable=False)
    category= db.Column(db.String(50))
    publisher= db.Column(db.String(100))
    stock= db.Column(db.Integer, default=1)
    
    def __repr__(self):
        return f"<Book {self.title}>"
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(50),unique=True,nullable=False)
    email= db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"