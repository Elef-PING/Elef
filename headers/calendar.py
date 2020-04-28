#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy
# authors @LeoDPlouc

import output as out 
from datetime import datetime
import pickle as pck
from io import FileIO as file

CALENDAR_PATH = "../files/calender.cal"

class Date:
    def __init__(self, date = datetime, title = str, message = str):
        self.date = date
        self.title = title
        self.message = message

    def __str__(self):
        return "{0} : {1}, {2}".format(str(self.date), self.title, self.message)

def save(dateObject = Date):
    l = list(load())
    l.append(dateObject)
    f = file(CALENDAR_PATH, "w")
    pck.dump(l, f)

def load():
    f, r = None, None
    try:
        f = file(CALENDAR_PATH, "r")
        r = pck.load(f)
    except:
        r = list()
    return r