# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///application.db'
    SECRET_KEY = "MINHACHAVESECRETA"
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    TWITTER_CONSUMER_KEY = ''
    TWITTER_CONSUMER_SECRET = ''
    TWITTER_ACCESS_TOKEN_KEY = ''
    TWITTER_ACCESS_TOKEN_SECRET = ''

    # mongo details
    MONGO_DBNAME = 'twitter_sink'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017


class TestingConfig(Config):
    TESTING = True
