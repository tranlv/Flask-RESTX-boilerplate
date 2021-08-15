#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
from os import environ
from dotenv import load_dotenv

# third party modules

# own modules

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."

class BaseConfig:

    load_dotenv()

    API_LOG_INFO_LIST = ["/api/v1"]
    JSON_AS_ASCII = False

    # mysql configuration
    DB_USER = environ.get('DB_USER', '')
    DB_PASSWORD = environ.get('DB_PASSWORD', '')
    DB_HOST = environ.get('DB_HOST', '')
    DB_PORT = environ.get('DB_PORT', '3306')
    DB_NAME = environ.get('DB_NAME', 'hoovada')
    DB_CHARSET = 'utf8mb4'
    MAXIMUM_RETRY_ON_DEADLOCK = int(environ.get('MAXIMUM_RETRY_ON_DEADLOCK', 10))
    BCRYPT_LOG_ROUNDS = 13 # Number of times a password is hashed
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SENTRY_DSN = environ.get('SENTRY_DSN', '')
    TRANSLATION_PATH = environ.get('TRANSLATION_PATH', "./app/translations/")
    DEFAULT_TRANSLATION_LANGUAGE = 'en'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset={charset}'.format(
         user=BaseConfig.DB_USER,
         password=BaseConfig.DB_PASSWORD,
         host=BaseConfig.DB_HOST,
         port=BaseConfig.DB_PORT,
         name=BaseConfig.DB_NAME,
         charset=BaseConfig.DB_CHARSET
     )


class ProductionConfig(BaseConfig):
    """production configuration."""

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset={charset}'.format(
         user=BaseConfig.DB_USER,
         password=BaseConfig.DB_PASSWORD,
         host=BaseConfig.DB_HOST,
         port=BaseConfig.DB_PORT,
         name=BaseConfig.DB_NAME,
         charset=BaseConfig.DB_CHARSET
     )
