# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

class Color:
    PURPLE = '\033[95m'

import datetime
import os
import logging

_logger = logging.getLogger("TOPS")

# class Color:
#     PURPLE = '\033[95m'
#     CYAN = '\033[96m'
#     DARKCYAN = '\033[36m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     END = '\033[0m'
#
#     def __init__(self):
#        pass

def talog(*args):
    log = ""
    for arg in args:
        log += str(arg)
    _logger.info(log)
    #logs can be info, debug, error, critical and warning

def tadebug(*args):
    log = ""
    for arg in args:
        log += str(arg)
    _logger.debug(log)
    #logs can be info, debug, error, critical and warning

def tawarn(*args):
    log = ""
    for arg in args:
        log += str(arg)
    _logger.warning(log)
    # logs can be info, debug, error, critical and warning

def squareNumber(num): #For testing purposes
    return num ** 2
