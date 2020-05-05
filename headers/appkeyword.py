#!bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

import calendar

class appKeyword():
    def __init__(self, app : str, func : str, args : list):
        self.app = app
        self.func = func
        self.args = args

    def execute(self):
        if self.app == "calendar":
            if self.func == "create":
                event = calendar.Date(self.args[0], self.args[1], self.args[2])
                event.save()