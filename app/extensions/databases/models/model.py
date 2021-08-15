#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules

# third-party modules
import dateutil.parser

# own modules
from common.db import db

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


def catch(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return None

class Model(db.Model):
    """Class entity is parent class for all other class"""
    
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def _asdict(self):
        object_dict = {attr: catch(getattr, self, attr) for attr in dir(self) if not attr.startswith("__")}
        return object_dict
    
    def _from_dict(self, dictionary):
        def _traverse(key, element):
            if isinstance(element, dict):
                return key, self._from_dict(element)
            else:
                try: 
                    return key, dateutil.parser.isoparse(element)
                except Exception:
                    return key, element

        objd = dict(_traverse(k, v) for k, v in dictionary.items() if v is not None)
        self.update(objd)
        
    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)