#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


# Better solution is to override the restx JSON encoder
def resolve_lazy_error_message(messages):
    def _gen():
        for key, value in messages.items():
            if callable(value):
                yield key, value()
            else:
                yield key, value
    return dict(_gen())


def send_result(data=None, message='OK', code=200, status=True):

    res = {
        'status': status,
        'code': code,
        'message': message,
        'data': data,
    }
    return res, code


def send_error(data=None, message='Failed', code=400, status=False):

    if isinstance(message, dict):
        message = resolve_lazy_error_message(message)

    res = {
        'status': status,
        'code': code,
        'message': message,
        'data': data,
    }
    return res, code


def paginated_result(query=None, message='OK', code=200, status=True):

    res = {
        'status': status,
        'code': code,
        'message': message,
        'page': query.page,
        'page_count': query.pages,
        'total': query.total,
        'data': query.items,
    }
    return res, code


def send_paginated_result(data=None, page=None, total=None, message='OK', code=200, status=True):

    res = {
        'status': status,
        'code': code,
        'message': message,
        'page': page,
        'total': total,
        'data': data,
    }

    return res, code


