from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(debug=True)


