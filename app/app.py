#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules

from logging.config import dictConfig
import re
# third-party modules
from flask import Flask, g, request, session, Response, current_app
from flask_cors import CORS
from sqlalchemy_utils import create_database, database_exists
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# own modules
from app import config_by_name
from app.extensions.utils.util import get_logged_user, get_client_ip
from app.extensions.databases.db import db
from app.extensions.databases.migrate import migrate
from app.extensions.observability.logging import logging
from app.extensions.i18n import configure_i18n
from app.config import BaseConfig

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


# Config logging output
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def log_request():
    if allow_to_log(request.path):
        client_ip = get_client_ip(request)
        get_values = dict(request.args)
        logger.info(f'CLIENT_IP: {client_ip}| PATH: {request.path}  | METHOD: {request.method}| ARGS: {get_values} | HEADER: {request.headers} ')


def log_response(response: Response):
    if allow_to_log(request.path):
        headers = list(response.headers)
        if int(response.status) not in [201, 200]:
            logger.info(f'Response: | PATH: {request.path} | STATUS: {response.status} | HEADERS: {headers} | DATA: {response.get_data(as_text=True)}')
    return response


def allow_to_log(path):
    for regex_pattern in current_app.config['API_LOG_INFO_LIST']:
        if re.match(regex_pattern, path):
            return True
    return False


sentry_sdk.init(
    dsn=BaseConfig.SENTRY_DSN,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)


def init_basic_app():

    Flask.get_logged_user = get_logged_user
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config_by_name[app.config['ENV']])

    @app.before_request
    def before_request():
        g.current_user = app.get_logged_user(request)

        if 'role' not in session:
            session['role'] = 'user'

        g.current_user_is_admin = g.current_user.admin if g.current_user is not None else False
        g.endorsed_topic_id = None
        g.friend_belong_to_user_id = None
        g.mutual_friend_ids = []

        # language can be extends to load from user setting, eg: user.setting.locate
        # or can be set to read default from accept-language header
        # this is from language query parameter
        language = request.args.get('language', BaseConfig.DEFAULT_TRANSLATION_LANGUAGE)
        configure_i18n(BaseConfig.TRANSLATION_PATH, locate=language)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    # app.before_request(log_request)
    # app.after_request(log_response)
    return app


# Prometheus metrics exporter
metrics = GunicornInternalPrometheusMetrics(init_basic_app())
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)


def init_app():
    app = init_basic_app()
    CORS(app)

    url = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(url):
        create_database(url, app.config['DB_CHARSET'])

    # for extension in (db, migrate, mail, logging):
    #     extension.init_app(app)

    return app
