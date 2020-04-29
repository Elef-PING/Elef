#!/bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

import json
from io import FileIO as file

CONFIGURE_PATH = "../files/.configure"
NAME_KEY = "name"
LANG_KEY = "lang"

def getConfigure():
    cf = None
    try:
        f = file(CONFIGURE_PATH, "r")
        cf = json.load(f)
    except:
        cf = {NAME_KEY: None, LANG_KEY: None}
    return cf

def setConfigure(configure = dict):
    f = file(CONFIGURE_PATH, "w")
    json.dump(configure, f)

def getName():
    cf = getConfigure()
    return cf[NAME_KEY]

def setName(name = str):
    cf = getConfigure()
    cf[NAME_KEY] = name
    setConfigure(cf)

def getLang():
    cf = getConfigure()
    return cf[LANG_KEY]

def setLang(lang = str):
    cf = getConfigure()
    cf[LANG_KEY] = lang
    setConfigure(cf)