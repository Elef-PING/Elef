#!bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

from abc import ABC, abstractmethod
from input import *

PATH = ../files/keywords.xml
LANG = "FR"

class Parser(Input):

	def __init__(self, inp):
		self.input = inp
		self.parsed = parser(self.inp)
		
		tmp = []
		with open(PATH, "r") as inp:
			for i in inp:
				i.find("kw")


	def evaluate(self):
		if parser(self) is not None:
			return 0

	def parser(self):
		parsed = None
		if isinstance(self, str):
			

