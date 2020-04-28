#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy
# authors @LeoDPlouc

import output as out 
from datetime import date
import pickle as pck
from io import FileIO as file

CALENDAR_PATH = "../files/calender.cal"

class Date:
    def __init__(self, date = date, title = str, message = str):
        self.date = datetime
        self.title = title
        self.message = message

    def __str__(self):
        return "{0} : {1}, {2}".format(str(self.date), self.title, self.message)

def save(dateObject = Date):
    f = file(CALENDAR_PATH, "a")
    pickler = pck.Pickler(f)
    pickler.dump(dateObject)
    f.close()