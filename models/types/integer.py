#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from formencode.validators import Int as fvInteger
from sqlalchemy import Column
from sqlalchemy import Integer as sqInteger
from sqlalchemy.orm import column_property

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '16.05.13 - 18:37'


def Integer(minval: int=None, maxval: int=None, default: int=None, *args, as_property:bool=True, info:dict=None, **kwargs):
    """
        SQLAlchemy Column representing an integer

        :param minval: minimum allowed for value
        :param maxval: maximum allowed for value
        :param default: default value (if None, nullable becomes True)
        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`

        :param args: any positional arguments are passed to the sqlalchemy.Column constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: * min: passed to :class:`formencode.validators.Integer` (and overrides minval)
                       * max: passed to :class:`formencode.validators.Integer` (and overrides maxval)
                       * else: passed to :class:`sqlalchemy.Column`

        :returns: >>> column_property(Column(Integer, nullable=False, default=default),
                  info={type='integer', min=minval, max=maxval, validator=Integer(min=minval, max=maxval)})
        :rtype: :class:`int`
    """

    fvargs = dict(min=minval, max=maxval)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict()
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=default is None, default=default)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqInteger(**sqargs), *args, **dwargs)
    column.validator = fvInteger(**fvargs)

    fmargs = {'type': 'Number', 'dataType': 'number', 'min': minval, 'max': maxval, 'step': 1.0}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs


def PositiveInteger(minval: int=0, maxval: int=None, default: int=None, *args, as_property:bool=True, info:dict=None, **kwargs):
    """
        SQLAlchemy Column representing a positive integer

        :param minval: minimum allowed for value
        :param maxval: maximum allowed for value
        :param default: default value (if None, nullable becomes True)
        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`

        :param args: any positional arguments are passed to the sqlalchemy.Column constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: * min: passed to formencode.validators.Integer (and overrides minval)
                       * max: passed to formencode.validators.Integer (and overrides maxval)
                       * else: passed to sqlalchemy.Column

        :returns: >>> column_property(Column(Integer, nullable=False, default=default),
                  info={type='integer', min=minval, max=maxval, validator=Integer(min=minval, max=maxval)})
        :rtype: :class:`int`
    """

    fvargs = dict(min=minval, max=maxval)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict()
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=default is None, default=default)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqInteger(**sqargs), *args, **dwargs)
    column.validator = fvInteger(**fvargs)

    fmargs = {'type': 'Number', 'dataType': 'number', 'min': minval, 'max': maxval, 'step': 1.0}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs