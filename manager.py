# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config



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

