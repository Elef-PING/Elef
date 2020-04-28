#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy
# authors @LeoDPlouc

import output as out 
import datetime as dt

class Date:
    def __init__(self, datetime, title, message):
        self.date = datetime
        self.title = title
        self.message = message

    def __str__(self):
        return "{0} : {1}, {2}".format(str(self.date), self.title, self.message)