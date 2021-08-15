#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules
from flask_migrate import Migrate

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


migrate = Migrate(compare_type=True)