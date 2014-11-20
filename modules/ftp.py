#!/usr/bin/env python
"""
version.py - jenni Version Module
Copyright 2009-2013, Michael Yanovich (yanovich.net)
Copyright 2009-2013, Silas Baronda
Licensed under the Eiffel Forum License 2.

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

from datetime import datetime
from subprocess import *




def ftp(jenni, input):

    jenni.say(str(input.nick) + " current ftp credentials are U: install P: gen4")
ftp.commands = ['ftp']
ftp.priority = 'medium'
ftp.rate = 30


if __name__ == '__main__':
    print __doc__.strip()
