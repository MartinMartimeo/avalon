#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:38'

from sqlalchemy import schema, text, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr

metadata = schema.MetaData()


class Base(object):
    """
        Base class for all database models
    """

    @declared_attr
    def __table_args__(cls):
        return {'useexisting': True}


    def __asdict__(self):
        values = vars(self)
        for attr in self.__mapper__.columns.keys():
            if attr in values:
                yield attr, values[attr]

    @declared_attr
    def created(self):
        """
            Creation Time of object
        """
        from .types.date import DateTime

        return DateTime(server_default=func.now(), info=dict(readonly=True))

    @declared_attr
    def modified(self):
        """
            Modification Timestamp
        """
        from .types.date import DateTime

        return DateTime(server_default=func.now(), server_onupdate=func.now(), info=dict(readonly=True))

    def __repr__(self):
        return "<%s %s />" % (self.__class__.__name__, " ".join("%s='%s'" % (k, v) for k, v in self.__asdict__()))


Base = declarative_base(metadata=metadata, cls=Base)

