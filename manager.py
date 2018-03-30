# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from iHome import db, create_app
from iHome import models

app = create_app("development")
from iHome import  redis_store
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    print app.url_map
    app.run()
    # manager.run()

