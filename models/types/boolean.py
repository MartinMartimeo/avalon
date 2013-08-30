#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from formencode.validators import StringBool as fvBoolean
from sqlalchemy import Column
from sqlalchemy import Boolean as sqBoolean
from sqlalchemy.orm import column_property

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '27.05.13 - 16:45'


def Boolean(default: bool=False, nullable=False, *args, **kwargs):
    """
        SQLAlchemy Column representing a boolean

        :param default: default of this column
        :param nullable: accept None -> NULL values

        :param args: any positional arguments are passed to the :class:`sqlalchemy.Column constructor`

        :param kwargs: * true_values: list of true string values, passed to formencode validator
                       * false_values: list of false string values, passed to formencode validator
                       * create_constraint: create a CHECK constraint if required, passed to sqlalchemy.Boolean
                       * else: passed to sqlalchemy.Column

        :returns: >>> column_property(Column(Boolean, nullable=False, default=default, server_default=default),
                  info={type='boolean', validator=Boolean()})
        :rtype: :class:`bool`
    """

    fvargs = dict(true_values=fvBoolean.true_values, false_values=fvBoolean.false_values)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict(create_constraint=True)
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(default=default, nullable=nullable)
    if default is not None:
        dwargs['server_default'] = "%s" % int(default)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqBoolean(**sqargs), *args, **dwargs)
    column.validator = fvBoolean(**fvargs)

    fmargs = {'type': 'CheckBox'}
    return column_property(column, info=fmargs)
