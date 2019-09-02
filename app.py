import json
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

with open('secret_key.json') as f:
  secret_key = json.load(f)
  
app.config['SECRET_KEY'] = json.dumps(secret_key)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.string(20), unique=True, nullable=False)
  email = db.Column(db.String(150), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"

posts = [
  {
    'author': 'Gabriel Sinca',
    'title': 'First blog post',
    'content': 'Insert some interesting content here',
    'date_posted': 'August 31, 2019'
  },
  {
    'author': 'Joe Doe',
    'title': 'Second blog post',
    'content': 'Insert more interesting content here',
    'date_posted': 'September 1, 2019'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/join", methods=['GET', 'POST'])
def join():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('join.html', title='Join', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  # BAD CODE; ONLY TESTING; DELETE LATER
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login unsuccessful. Please check username and passowrd', 'danger')
  return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(debug=True)


