# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from iHome import db, app, redis_store


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

