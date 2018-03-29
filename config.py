# -*- coding:utf-8 -*-

import redis

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



class DevelopmentConfig(Config):
    DEBUG=True


class ProductionConfig(Config):
    pass