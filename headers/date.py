#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy
# authors @LeoDPlouc

import output.py as out
import datetime as dt

class Date:
    def __init__(self, datetime, title, message):
        self.date = datetime
        self.title = title
        self.message = message