#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules

# own modules
from app.extensions.api.dto import Dto
from flask_restx import Namespace

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


class SampleDto(Dto):
    api = Namespace('sample')
