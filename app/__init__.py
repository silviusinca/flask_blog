from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

with open('secret_key.json') as f:
  secret_key = json.load(f)
  
app.config['SECRET_KEY'] = json.dumps(secret_key)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from app import routes
