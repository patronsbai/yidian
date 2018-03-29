# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(DevelopmentConfig.REDIS_HOST, DevelopmentConfig.REDIS_PORT)
csrf = CSRFProtect(app)
Session(app)