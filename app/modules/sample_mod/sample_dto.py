#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules

# own modules
from app.extensions.api.dto import Dto
from flask_restx import Namespace

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


class SampleDto(Dto):
    api = Namespace('sample')
