# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):

    DEBUG=True
    SECRET_KEY = "sdgvsdvsdvsdvsv"

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:33006/ihome18"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(Config.REDIS_HOST, Config.REDIS_PORT)
csrf = CSRFProtect(app)
Session(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

@app.route("/index", methods=["GET", "POST"])
def index():
    redis_store.set("name", "baichongkun")
    return "index"

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()

