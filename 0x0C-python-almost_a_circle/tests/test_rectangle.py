#!/usr/bin/python3

import unittest
from models import rectangle
from models import base

Rectangle = rectangle.Rectangle
Base = base.Base


class TestRectangle(unittest.TestCase):
    """Check the funcionality of the rectangle"""
