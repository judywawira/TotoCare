import sys

from flask import Flask
from flask.ext.login import LoginManager
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)

mongo = PyMongo(app)
app.config['MONGO2_DBNAME'] = 'TotoCare'
mongo2 = PyMongo(app, config_prefix='MONGO2')

app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

""" Mongo Stuff"""
client = MongoClient('localhost:27017')
db = client.TotoCare

from app import views