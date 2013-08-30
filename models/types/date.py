#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
import datetime
from formencode import NoDefault, FancyValidator
from formencode.validators import DateConverter, TimeConverter
from sqlalchemy import Column
from sqlalchemy import Date as sqDate
from sqlalchemy import DateTime as sqDateTime
from sqlalchemy import Time as sqTime
from sqlalchemy.orm import column_property, ColumnProperty

__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '04.06.13 - 21:36'


class fvDate(DateConverter):
    """
        Parse a date
    """

    def __init__(self,
                 accept_date: bool=True,
                 month_style: str='dd/mm/yyyy',
                 datetime_module=None):

        super().__init__(accept_date=accept_date, month_style=month_style, datetime_module=datetime_module)

    def _convert_to_python(self, value, state) -> datetime.date:
        if isinstance(value, (datetime.datetime, datetime.date)):
            return value
        else:
            super()._convert_to_python(value=value, state=state)

    def _convert_from_python(self, value: datetime.datetime, state) -> str:
        return value.isoformat()


class fvTime(TimeConverter):
    """
        Parse a date
    """

    def __init__(self,
                 use_ampm: str='optional',
                 prefer_ampm: bool=False,
                 use_seconds: str='optional',
                 use_datetime: bool=False,
                 datetime_module=None):

        super().__init__(use_ampm=use_ampm, prefer_ampm=prefer_ampm,
                         use_seconds=use_seconds, use_datetime=use_datetime, datetime_module=datetime_module)

    def _convert_to_python(self, value, state) -> datetime.time:
        if isinstance(value, (datetime.datetime, datetime.time)):
            return value
        else:
            super()._convert_to_python(value=value, state=state)

    def _convert_from_python(self, value: datetime.datetime, state) -> str:
        return value.isoformat()


class fvDateTime(FancyValidator):
    """
        Parse a datetime
    """

    def __init__(self,
                 accept_date: bool=True,
                 month_style: str='dd/mm/yyyy',
                 use_ampm: str='optional',
                 prefer_ampm: bool=False,
                 use_seconds: str='optional',
                 use_datetime: bool=False,
                 datetime_module=None,
                 *args, **kw):

        super().__init__(*args, **kw)

        # Create sub validator
        self.date = fvDate(accept_date=accept_date, month_style=month_style, datetime_module=datetime_module)
        self.time = fvTime(use_ampm=use_ampm, prefer_ampm=prefer_ampm,
                           use_seconds=use_seconds, use_datetime=use_datetime, datetime_module=datetime_module)

    def _convert_to_python(self, value, state) -> datetime:
        if isinstance(value, (datetime.datetime, datetime.time, datetime.date)):
            return value
        try:
            date, time = value.split(" ")
            return self.date.to_python(date) + self.time.to_python(time)
        except ValueError:
            if self.if_invalid != NoDefault:
                return self.if_invalid
            else:
                raise

    def _convert_from_python(self, value: datetime.datetime, state) -> str:
        return value.isoformat()


def Date(*args, month_style: str='dd/mm/yyyy', as_property:bool=True, info:dict=None, **kwargs) -> ColumnProperty:
    """
        SQLAlchemy Column representing a date

        :param month_style: passed to formencode.validators.DateConverter
        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`

        :param args: any positional arguments are passed to the sqlalchemy.Column constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: passed to sqlalchemy.Column

        :returns: >>> column_property(Column(Date, nullable=False), info={type='date', validator=DateConverter()})
        :rtype: :class:`datetime.date`

    """

    fvargs = dict(month_style=month_style)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict()
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=False)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqDate(**sqargs), *args, **dwargs)
    column.validator = fvDate(**fvargs)

    fmargs = {'type': 'Date'}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs


def DateTime(*args, month_style: str='dd/mm/yyyy', as_property:bool=True, info:dict=None, **kwargs) -> ColumnProperty:
    """
        SQLAlchemy Column representing a datetime

        :param month_style: passed to formencode.validators.DateConverter
        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`

        :param args: any positional arguments are passed to the sqlalchemy.Column constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: passed to sqlalchemy.Column

        :returns: >>> column_property(Column(Date, nullable=False), info={type='date', validator=DateTimeConverter()})
        :rtype: :class:`datetime.datetime`
    """

    fvargs = dict(month_style=month_style)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict()
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=False)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqDateTime(**sqargs), *args, **dwargs)
    column.validator = fvDateTime(**fvargs)

    fmargs = {'type': 'DateTime'}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs


def Time(*args, use_datetime: bool=True, as_property:bool=True, info:dict=None, **kwargs):
    """
        SQLAlchemy Column representing a time

        :param use_datetime: passed to :class:`formencode.validators.DateConverter`
        :param as_property: Returns :class:`sqlalchemy.ColumnProperty` otherwise :class:`sqlalchemy.Column`

        :param args: any positional arguments are passed to the :class:`sqlalchemy.Column` constructor

        :param info: Passed into info dictionary of the column for usage with form maker or similiar libaries

        :param kwargs: passed to :class:`sqlalchemy.Column`

        :returns: >>> column_property(Column(Date, nullable=False),
                  info={type='date', validator=TimeConverter(use_datetime=True)})
        :rtype: :class:`datetime.time`
    """

    fvargs = dict(use_datetime=use_datetime)
    fvargs.update({k: v for k, v in kwargs.items() if k in fvargs})

    sqargs = dict()
    sqargs.update({k: v for k, v in kwargs.items() if k in sqargs})

    dwargs = dict(nullable=False)
    dwargs.update({k: v for k, v in kwargs.items() if k not in fvargs and k not in sqargs})

    column = Column(sqTime(**sqargs), *args, **dwargs)
    column.validator = fvTime(**fvargs)

    fmargs = {'type': 'Time'}
    fmargs.update(info and info or {})
    if as_property:
        return column_property(column, info=fmargs)
    else:
        column.info.update(fmargs)
        return column, fmargs