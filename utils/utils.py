# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later
import uuid

class Color:
    PURPLE = '\033[95m'

from datetime import datetime, time, timedelta
import os
import logging
import qrcode
import base64
from io import BytesIO

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

def taerror(*args):
    log = ""
    for arg in args:
        log += str(arg)
    _logger.error(log)
    # logs can be info, debug, error, critical and warning

def generate_qr(url):
    print("????? Generating QR code")
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format='PNG')
    qr_bytes = buf.getvalue()
    print("{{{{{{{{{{{{{{", base64.b64encode(qr_bytes).decode("utf-8"))

    return base64.b64encode(qr_bytes).decode("utf-8")

def generate_UUID():
    return(uuid.uuid4())

def get_datetime_date_to_epoch(my_date):
    #time.min represents the minimum time in the day, and sets the epoch time to the beginning of the specified day
    return int(datetime.combine(my_date, time.min).timestamp())

def get_datetime_now_to_epoch(add_minutes):
    return int((datetime.now() + timedelta(minutes=add_minutes)).timestamp())
