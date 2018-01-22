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
    TWITTER_CONSUMER_KEY = 'nLN1HuGpCog4n2y1eCy0y1o4e'
    TWITTER_CONSUMER_SECRET = 'g4WuYpr1bk5odUFt2dVh4Uroec8TKNNZjAam5KBkj7QPPbHDxM'
    TWITTER_ACCESS_TOKEN_KEY = '955356200975065088-RoB1VqwVFIpr8fvC417ySwD9HekkWRm'
    TWITTER_ACCESS_TOKEN_SECRET = 'ayBVJRmxbj0Cx3AUqE7ZmpqWTf2JDfINOCiuRop5UF6Bn'

    # mongo details
    MONGO_DBNAME = 'twitter_sink'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017


class TestingConfig(Config):
    TESTING = True
