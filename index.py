from flask import Flask
from flask import render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap
import calendar
from datetime import datetime
import pytz
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = '認証していません：ログインしてください'
login_manager.login_view = 'login'


class Posts(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(pytz.timezone('Asia/Tokyo')))


class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(15))


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def front():
    dt = datetime.now(pytz.timezone('Asia/Tokyo'))
    year, month = dt.year, dt.month
    cln = calendar.HTMLCalendar(firstweekday=6)
    return render_template('front.html', year=year,
                           month=month, cln=cln)


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        posts = Posts.query.all()
        dt = datetime.now(pytz.timezone('Asia/Tokyo'))
        year, month = dt.year, dt.month
        cln = calendar.HTMLCalendar(firstweekday=6)
        return render_template('index.html', posts=posts, year=year,
                               month=month, cln=cln)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print('form', request.form)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('notice', username, len(username))
        if username == '' or password == '':
            flash('※ユーザー名もしくはパスワードが有効ではありません')
            flash('※違うユーザー名、パスワードをお使いください')
            return redirect('/signup')
        elif Users.query.filter_by(username=username).first():
            flash('※そのユーザー名は既に使用されています')
            return redirect('/signup')
        else:
            user = Users(username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(user)
            db.session.commit()
        return redirect('/login')
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            return redirect('/index')
        else:
            flash("※ユーザー名もしくはパスワードが違います")
            return redirect('/login')
    else:
        return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("ログアウト完了しました")
    return redirect('/login')


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        post = Posts(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create.html')


@app.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    post = Posts.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        db.session.commit()
        return redirect('/index')


@app.route('/<int:id>/delete', methods=['GET'])
@login_required
def delete(id):
    post = Posts.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/index')


@app.errorhandler(404)
def show_404_page(error):
    msg = error.description
    print('エラー内容:', msg)
    return render_template('404.html')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
