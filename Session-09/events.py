# ---------------------------------------------------------------------
# Filename      : events.py
# Location      : ./Session-09
# Project       : Class-Examples
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 16/9/21
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------
import datetime


class Event:
    location = None
    timestamp = None #datetime.datetime.timestamp()
    presence = False
    sensor = None
