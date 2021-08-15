#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules

# third-party modules
from flask import g
from functools import wraps
from marshmallow import ValidationError

# own modules
from app.extensions.utils.response import send_error
from app.extensions.i18n import i18n

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        user = g.current_user
        if user is None:
            return send_error(
                message=i18n.t("authentication.error.not_login"), code=401
            )
        if user.is_deactivated:
            return send_error(
                message=i18n.t("authentication.error.user_deactivated"),
                code=401
            )
        return f(*args, **kwargs)

    return decorated


def validate_payload(schema_cls):

    def inner(f):
        @wraps(f)
        def decorated(self, data, *args, **kwargs):
            if not isinstance(data, dict):
                return send_error(
                    message=i18n.t("validation.error.wrong_data_format")
                )

            try:
                validated_data = schema_cls().load(data)
            except ValidationError as err:

                return send_error(
                    message=err.messages
                )

            return f(self, validated_data, *args, **kwargs)
        return decorated
    return inner
