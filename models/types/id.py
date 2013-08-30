#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer as sqInteger
from sqlalchemy import String as sqString

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '06.04.13 - 20:19'


def Id(name: str, *args, **kwargs):
    """
        Column representing an id

        :param name: Name of Id
        :param args: Additional Parameters passed to Column Instance
        :param kwargs: Additional Parameters passed to Column Instance
        :rtype: :class:`int`
    """

    dwargs = dict(primary_key=True, nullable=False)
    dwargs.update(kwargs)

    return Column(name, sqInteger, *args, **dwargs)


def IdString(name: str, *args, **kwargs):
    """
        Column representing an id

        :param name: Name of Id
        :param args: Additional Parameters passed to Column Instance
        :param kwargs: Additional Parameters passed to Column Instance
        :rtype: :class:`int`
    """

    dwargs = dict(primary_key=True, nullable=False)
    dwargs.update(kwargs)

    return Column(name, sqString, *args, **dwargs)


def ForeignId(name: str, reference, *args, **kwargs):
    """
        Foreign Key to another table

        :param name: Name of ForeignId
        :param reference: Table for Reference
        :param args: Additional Parameters passed to Column Instance
        :param kwargs: Additional Parameters passed to Column Instance
        :rtype: :class:`int`
    """

    dwargs = dict(index=True, nullable=False)
    dwargs.update(kwargs)

    self = Column(name, ForeignKey(reference, onupdate="CASCADE", ondelete="CASCADE"), *args, **dwargs)
    self.reference = reference

    return self