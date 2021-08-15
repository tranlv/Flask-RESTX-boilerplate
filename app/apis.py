#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
from os import environ

# third-party modules
from flask import url_for
from flask_restx import Api

# own modules
from app.modules import *
from app.extensions.utils.response import send_result

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


class HTTPSApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        return url_for(self.endpoint('specs'), _external=True, _scheme=environ.get('WEB_PROTOCOL', 'https'))


def init_api():
    api = HTTPSApi(title='Hoovada APIs',
                   version='1.0',
                   description='The Hoovada APIs',
                   authorizations={
                       'apikey': {
                           'type': 'apiKey',
                           'in': 'header',
                           'name': 'X-API-KEY'
                       }
                   },
                   security='apikey',
                   prefix='/api/v1',
                   doc='/api/v1/openapi')

    api.add_namespace(ns_sample, '/sample')
    return api
