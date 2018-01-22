import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)

#Configuration of application, see configuration.py.
env = os.environ.get('ENV', 'dev')

def get_config(env):
     return '.'.join(['app', 'configuration', '{}Config'.format(env.title())])

config = get_config(env)
app.config.from_object(config)

api = Api(app)
mongo = PyMongo(app)

from app.url_defs import *

