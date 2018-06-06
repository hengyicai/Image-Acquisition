# -*- encoding: utf-8 -*-
import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
from flask_dropzone import Dropzone
import sqlite3
from flask import g

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configuration of application, see configuration.py, choose one and uncomment.
# app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
# app.config.from_object('configuration.TestingConfig')

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)

bs = Bootstrap(app)  # flask-bootstrap
db = SQLAlchemy(app)  # flask-sqlalchemy
dropzone = Dropzone(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

DATABASE = './app/db/image_ac.db'


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


from app import views, models
