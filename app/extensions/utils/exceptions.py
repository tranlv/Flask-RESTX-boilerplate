#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules
import enum
from http import HTTPStatus
from typing import List
from flask_restplus import abort
from requests import HTTPError
from werkzeug.exceptions import HTTPException, Unauthorized


__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."



#from app.extension.observability.logging import loggers
#_logger = loggers.get('main')


class HTTPResponse:
    """Define base http response"""
    
    status_code: int
    code: str
    message: str
    extra: dict

    def __init__(self, status_code: int, code: str, message: str):
        if status_code:
            self.status_code = status_code
        if code:
            self.code = code
        if message:
            self.message = message


class SuccessResponse(HTTPResponse):
    def __init__(self, status_code=HTTPStatus.OK, code=HTTPStatus.OK.name, message=HTTPStatus.OK.name):
        super().__init__(status_code, code, message)


class ApplicationError(Exception, HTTPResponse):
    code = 'APPLICATION_ERROR'

    def __init__(self, message=HTTPStatus.INTERNAL_SERVER_ERROR.name):
        if message:
            self.message = message
        # super(ApplicationError, self).__init__(status_code, code, message)

    def __repr__(self):
        return f"<ApplicationError {self.message}>"


class MalformedEventError(ApplicationError):
    pass


class MalformedCommandError(ApplicationError):
    pass


class MalformedDataError(ApplicationError):
    pass


class MalformedConnectionError(ApplicationError):
    pass


class CommandValidationError(ApplicationError):
    pass


class HandlerNotFoundError(ApplicationError):
    pass


class ConvertError(ApplicationError):
    pass


class UserInputSchemaError(ApplicationError):
    pass


class ChangeOnOldVersionError(ApplicationError):
    pass


class StructureError(ApplicationError):
    pass


class UnexpectedError(ApplicationError):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    code = 'UNKNOWN_ERROR'
    message = HTTPStatus.INTERNAL_SERVER_ERROR.name


class BadGateWayError(Exception, HTTPResponse):
    code = HTTPStatus.BAD_GATEWAY.name

    def __init__(self, message=HTTPStatus.BAD_GATEWAY.name):
        if message:
            self.message = message
        # super(ApplicationError, self).__init__(status_code, code, message)

    def __repr__(self):
        return f"<ApplicationError {self.message}>"


class ClientError(HTTPException, HTTPResponse):
    status_code = HTTPStatus.BAD_REQUEST
    extra = None
    code = HTTPStatus.BAD_REQUEST.name

    def __init__(self, message=HTTPStatus.BAD_REQUEST.name, code=None, description=None,
                 response=None, extra=None):
        if code:
            self.code = code
        self.message = message
        if extra:
            self.extra = extra
        super(ClientError, self).__init__(description=description, response=response)

    def __repr__(self):
        return f"<ClientError {self.message}>"


class LogicalValidationError(ClientError):
    status_code = HTTPStatus.BAD_REQUEST
    pass


class NotFoundError(ClientError):
    status_code = HTTPStatus.NOT_FOUND
    code = HTTPStatus.NOT_FOUND.name


class MethodIsNotAllowedException(ClientError):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    code = HTTPStatus.METHOD_NOT_ALLOWED.name

    def __init__(self, method, allowed_methods: List = None):
        super().__init__()
        self._error.update({'message': f'Method {method} is not allowed'})
        if allowed_methods is not None and any(allowed_methods):
            self._error['allowed_methods'] = allowed_methods


#
# class InvalidParametersException(ClientError):
#     status_code = HTTPStatus.INVALID_PARAMETERS
#     code = HTTPStatus.BAD_REQUEST.name
#
#     def __init__(self, error):
#         super().__init__()
#         self._error['message'] = 'Invalid parameter'
#         self._error['detail'] = error
#

class UnauthorizedException(ClientError):
    status_code = HTTPStatus.UNAUTHORIZED
    code = HTTPStatus.UNAUTHORIZED.name



class PermissionDeniedException(ClientError):
    status_code = HTTPStatus.FORBIDDEN
    code = HTTPStatus.FORBIDDEN.name

#
# class ClientDeniedException(ClientError):
#     status_code = HTTPStatus.CLIENT_DENIED
#     code = HTTPStatus.FORBIDDEN.name
#
#
# class IpAddressDeniedException(ClientError):
#     status_code = HTTPStatus.IP_ADDRESS_DENIED
#     code = HTTPStatus.FORBIDDEN.name
#
#     def __init__(self, ip_address):
#         super().__init__()
#         self._error['message'] = f'IP Address {ip_address} is not allowed'
#

class ClientBadRequestException(ClientError):
    status_code = HTTPStatus.BAD_REQUEST
    code = HTTPStatus.BAD_REQUEST.name
