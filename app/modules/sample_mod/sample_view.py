#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules
from os import environ
from flask import request
from flask_restx import Resource, fields

# own modules

from app.extensions.utils.decorator import token_required
from app.modules.sample_mod.sample_controller import SampleController
from app.modules.sample_mod.sample_dto import SampleDto
from app.modules.sample_mod.datadef import EmailRegistrationSchema


__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


api = SampleDto.api


@api.route('/whoami', methods=['GET'])
class WhoAmI(Resource):
    @api.doc(
        params={'id': 'An ID'},
        responses={403: 'Not Authorized'}
    )
    def get(self):
        user = environ.get("USER", "UNKNOW")
        data = {
            "message": f"You are: {user}"
        }
        return data


@api.route('/swagger-doc', methods=['GET'])
class DummyDoc(Resource):
    @api.doc(
        params={'abitrary_id': 'abitrary_id'},
        responses={200: 'OK'}
    )
    def get(self):
        user = environ.get("USER", "UNKNOW")
        data = {
            "message": f"Hello: {user}"
        }
        return data


@api.route('/register', methods=['POST'])
class Register(Resource):
    # this is for swagger doc, no other meaning
    @api.expect(EmailRegistrationSchema().to_flask_restx_model(api))
    def post(self):
        return SampleController().register(api.payload)
