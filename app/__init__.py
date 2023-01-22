import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.app_context().push()
app.config.from_prefixed_env()

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

from app.models import Authors
from app.models import Articles
from app.models import Tags
from app import views
from app.admin import *
