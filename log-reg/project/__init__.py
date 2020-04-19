import os,sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev')

db = SQLAlchemy(app)



from project import views, errors, commands