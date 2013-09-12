#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from formencode.validators import String as fvString
from sqlalchemy import Column
from sqlalchemy import Unicode as sqUnicode
from sqlalchemy.orm import column_property

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '13.04.13 - 16:13'


def String(maxlen: int=None, minlen: int=None,
           args: tuple=None, as_property: bool=True, info: dict=None, **kwargs):
    """
        SQLAlchemy Column representing a string

        :param minlen: minimum string len
        :param maxlen: maximum string len

        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`
        :param args: positional arguments passed to the sqlalchemy.Column constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: * min: passed to formencode.validators.String (and overrides minlen)
                       * max: passed to formencode.validators.String (and overrides maxlen)
                       * length: passed to sqlalchemy.String (and overrides maxlen)
                       * collation: passed to sqlalchemy.Unicode
                       * convert_unicode: passed to sqlalchemy.Unicode
                       * unicode_error: passed to sqlalchemy.Unicode
                       * else: passed to sqlalchemy.Column

        :returns: >>> column_property(Column(Unicode(maxlen), nullable=False, server_default=''),
                  info={type='string', validator=String(min=minlen, max=maxlen)})
        :rtype: :class:`str`
    """

    fvargs = dict(min=minlen, max=maxlen)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict(length=maxlen, collation=None, convert_unicode=True, unicode_error=None)
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=False, server_default='')
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    args = isinstance(args, tuple) and args or [args]

    column = Column(sqUnicode(**sqargs), *args, **dwargs)
    column.validator = fvString(**fvargs)

    fmargs = {'type': 'Text', 'dataType': 'text'}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs

