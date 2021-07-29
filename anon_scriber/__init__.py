import os
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import requests

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '88948ab134d6c6bab5b41493'

db = SQLAlchemy(app)

Migrate(app, db)

bcrypt = Bcrypt(app) # Used to hash stored passwords

login_manager = LoginManager(app)
login_manager.login_view = "login_page" # This line will redirect user when user tries to access unauthorized pages
login_manager.login_message_category = 'warning' # This line will display an error message during unauthorized access

from anon_scriber import routes
