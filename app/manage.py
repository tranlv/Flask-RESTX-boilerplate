#!/usr/bin/env python
# -*- coding: utf-8 -*-

# own modules
from app.app import init_app
from app.apis import init_api


__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


def create_app():
    app = init_app()
    api = init_api()
    api.init_app(app)
    return app


flask_app = create_app()


@flask_app.route('/healthz')
def __health():
    return 'ok'


@flask_app.route('/ready')
def __ready():
    return check_app_ready()


@flask_app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
