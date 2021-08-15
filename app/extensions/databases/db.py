#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third-party modules
from sqlalchemy import engine, MetaData
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from flask_migrate import Migrate

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


def get_model(self, name):
    return self.Model._decl_class_registry.get(name, None)


def get_model_by_tablename(self, tablename):
    for c in self.Model._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c

class AlembicDatabaseMigrationConfig(object):
    """
    Helper config holder that provides missing functions of Flask-Alembic
    package since we use custom invoke tasks instead.
    """

    def __init__(self, database, directory='migrations', **kwargs):
        self.db = database  # pylint: disable=invalid-name
        self.directory = directory
        self.configure_args = kwargs

        
class SQLAlchemy(BaseSQLAlchemy):
    """
    Customized Flask-SQLAlchemy adapter with enabled autocommit, constraints auto-naming conventions .
    """

    def __init__(self, *args, **kwargs):
        if 'session_options' not in kwargs:
            kwargs['session_options'] = {}
        kwargs['session_options']['autocommit'] = True
        # Configure Constraint Naming Conventions:
        # http://docs.sqlalchemy.org/en/latest/core/constraints.html#constraint-naming-conventions
        kwargs['metadata'] = MetaData(
            naming_convention={
                'pk': 'pk_%(table_name)s',
                'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
                'ix': 'ix_%(table_name)s_%(column_0_name)s',
                'uq': 'uq_%(table_name)s_%(column_0_name)s',
                'ck': 'ck_%(table_name)s_%(constraint_name)s',
            }
        )
        super(SQLAlchemy, self).__init__(*args, **kwargs)

    def init_app(self, app):
        super(SQLAlchemy, self).init_app(app)
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        assert database_uri, "SQLALCHEMY_DATABASE_URI must be configured!"
        app.extensions['migrate'] = AlembicDatabaseMigrationConfig(self, compare_type=True)

SQLAlchemy.get_model = get_model
SQLAlchemy.get_model_by_tablename = get_model_by_tablename

db = SQLAlchemy()
