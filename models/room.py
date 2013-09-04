#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 18:41'

from . import Base
from .types.id import Id
from .types.string import String
from .types.date import DateTime


class DbRoom(Base):
    """
        Represents a room where people can join for a game
    """

    __tablename__ = "room"

    def __init__(self):
        pass

    _id = Id("room_id")

    name = String(maxlen=80, unique=True)
    name.doc = "Name of the Room for display"

