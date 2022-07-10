#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules

# third-party modules

# own modules
from app.extensions.api.controller import Controller
from app.modules.sample_mod.datadef import EmailRegistrationSchema
from app.extensions.utils.decorator import validate_payload

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


class SampleController(Controller):

    @validate_payload(EmailRegistrationSchema)
    def register(self, data):
        return data

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass
