#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '04.09.13 - 17:29'

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from . import Base
from .room import DbRoom
from .types.id import Id
from .types.integer import Integer
from .types.string import String


class DbUser(Base):
    """
        A user in our system
    """

    __tablename__ = "user"

    def __init__(self):
        super().__init__()

        self.token = uuid4()

    _id = Id("user_id")

    name = String(maxlen=80, unique=True)
    name.doc = "Name of the User"

    _room_id = Integer(ForeignKey(DbRoom._id), name="room_id", nullable=True)
    _room_id.doc = "Room the user currently is in"

    room = relationship(DbRoom, backref="users")
    room.doc = "Room of user"

    token = String()
    token.doc = "A security by obscurity token that you need to pass for user modifications"



