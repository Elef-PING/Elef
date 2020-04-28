#!bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

from abc import ABC, abstractmethod
from inputBase import *

class Input(InputBase):
	
	def __init__(self, inp):
		self.input = inp
		self.parsed = parse(self.inp)

	def execute(self):
		return parse(self.inp)

	def parse():
		pass
