from flask import Flask, redirect,render_template,request,url_for,flash
from extensions import db #veri tabanı bağlantısı
from forms import BookForm
from dotenv import load_dotenv
import os

app=Flask(__name__)


# Veritabanı bağlantısı
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False #SQLAlchemy’nin model değişikliklerini izleme özelliğini kapatır (performans için False önerilir)
app.secret_key= os.getenv("SECRET_KEY")

db.init_app(app)

from models import Book,User

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    books= Book.query.all()
    return render_template("index.html", books=books)

#Add book
@app.route("/add", methods=["POST","GET"])
def add_book():
    form = BookForm()
    if request.method == "POST":
        title=  request.form["title"]
        author= request.form["author"]
        #category= request.form["category"]
        #publisher= request.form["publisher"]
        stock= request.form["stock"]
        
        new_book= Book(title=title, author=author,stock=stock)#category=category,publisher=publisher,
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for("index"))
    return render_template("add_book.html",form=form)

#Delete book
@app.route("/delete/<int:id>")
def delete_book(id):
    book= Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))

#Edit book
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit_book(id):
    book=Book.query.get(id)
    if request.method== "POST":
        book.title= request.form["title"]
        book.author= request.form["author"]
        #book.category= request.form["category"]
        #book.publisher= request.form["publisher"]
        book.stock= request.form["stock"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_book.html",book=book)


#Authentication
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,login_user,login_required,current_user,logout_user
from forms import RegisterForm,LoginForm

#Authentication connect
bcrypt=Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view="login"
login_manager.login_message="Lütfen giriş yapınız."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get((int(user_id)))

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Aynı e-postaya sahip kullanıcı var mı?
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("❗ Bu e-posta adresiyle zaten bir hesap var. Lütfen giriş yapın.", "warning")
            # Sayfada kal, yönlendirme yapma
            return render_template("register.html", form=form)

        # Yeni kullanıcı oluştur
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("✅ Kayıt başarılı! Giriş yapabilirsiniz.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)



@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)