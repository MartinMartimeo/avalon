#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 17:57'

import os
import site
import sys

# Ensure Python 3
if sys.hexversion < 0x03030000:
    raise SystemError("Not started with minimum Python 3.3")

from base.application import Application

from tornado.options import define, options, parse_command_line
define("port", default=4070, help="run on the given port", type=int)

# Add Apis
for api in next(os.walk(os.path.join(os.path.dirname(__file__), "api")))[1]:
    site.addsitedir(os.path.join(os.path.dirname(__file__), "api", api))

if __name__ == "__main__":
    parse_command_line()

    app = Application()
    app.listen(options.port)
    app.start()
