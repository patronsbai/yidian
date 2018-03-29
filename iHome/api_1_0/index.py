# -*- coding:utf-8 -*-

from . import api
from iHome import redis_store


@api.route("/index", methods=["GET", "POST"])
def index():
    redis_store.set("name", "baichongkun")
    return "index11111"