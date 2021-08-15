#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
from abc import ABC

# third-party modules

# own modules

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


class Controller(ABC):
    def create(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
    	pass

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass