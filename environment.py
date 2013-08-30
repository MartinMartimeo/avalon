#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    Some variables
"""
__author__ = 'Martin Martimeo <martin@martimeo.de>'
__date__ = '30.08.13 - 17:57'

import os

# The Port
port = 4070

# Static Path
static_path = os.path.join(os.path.dirname(__file__), "static")

# Template Path
template_path = os.path.join(os.path.dirname(__file__), "templates")

# Database connection
dns = 'sqlite:///:memory:'

# Languages we support
langs = ['en']

# Clean up imported modules
del os