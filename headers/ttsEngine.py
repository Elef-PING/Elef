#!bin/python3
# -*- coding: utf-8 -*-
#authors @LeoDPlouc

import platform
import pyttsx3 as tts

engine = tts.init()

def speak(text : str):
    engine.say(text)
    engine.runAndWait()