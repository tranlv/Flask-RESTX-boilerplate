#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
from abc import ABC, abstractmethod

# third-party modules
from flask_restx import reqparse

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""

class Dto(ABC):

    paginated_request_parser = reqparse.RequestParser()
    paginated_request_parser.add_argument('page', type=int, required=False, help='Page number.')
    paginated_request_parser.add_argument('per_page', type=int, required=False, help='Number of results per page.')
    paginated_request_parser.add_argument('from_created_date', type=int, required=False, help='Get from created_date')
    paginated_request_parser.add_argument('to_created_date', type=int, required=False, help='Get to created_date')
