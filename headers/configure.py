#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

import json
from io import FileIO as file

CONFIGURE_PATH = "../files/.configure"

def getConfigure():
    cf = None
    try:
        f = file(CONFIGURE_PATH, "r")
        cf = json.load(f)
    except:
        cf = {"name": None, "lang": None}
    return cf

def setConfigure(configure = dict):
    f = file(CONFIGURE_PATH, "w")
    json.dump(configure, f)

def getName():


def setName(name = str):
