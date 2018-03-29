# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config

db = None
redis_store = None
csrf = None

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    global db
    db = SQLAlchemy(app)

    global redis_store
    redis_store = redis.StrictRedis(config[config_name].REDIS_HOST, config[config_name].REDIS_PORT)

    global csrf
    csrf = CSRFProtect(app)

    Session(app)

    return app