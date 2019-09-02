from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import json

app = Flask(__name__)

with open('secret_key.json') as f:
  secret_key = json.load(f)
  
app.config['SECRET_KEY'] = json.dumps(secret_key)

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


