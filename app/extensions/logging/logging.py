#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in modules
import logging

# third-party modules

# own modules

__author__ = ""
__maintainer__ = ""
__email__ = ""
__copyright__ = ""


class Logging(object):

	def __init__(self, app=None):
		if app:
			self.init_app(app)

	def init_app(self, app):
		"""Common Flask interface to initialize the logging according to the application configuration."""

		# remove Flask log handler
		for handler in list(app.logger.handlers):
			app.logger.removeHandler(handler)
		app.logger.propagate = True

		app.logger.setLevel(logging.DEBUG)

		# remove sqlalchemy loghanler
		sqlalchemy_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
		for hdlr in list(sqlalchemy_logger.handlers):
			sqlalchemy_logger.removeHandler(hdlr)
		sqlalchemy_logger.addHandler(logging.NullHandler())


