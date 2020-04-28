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
		self.keywords = []
		
		tmp = []
		with open(PATH, "r") as keywordsfile:
			for i in keywordsfile:
				index1, index2 = i.find("kw"), i.find("lang")
				if index2 == -1:
					tmp.append(i.split("\"")[1])
				elif index1 == -1:
					if i[12:13] == LANG:
						tmp.append(i.split(">")[1].split("<")[0])
						self.keywords.append(tmp)
						tmp = []
				elif index1 == -1 && index2 == -1:
					print("file error")


	def evaluate(self):
		if parser(self) is not None:
			return 0

	def parser(self):
		parsed = None
		if isinstance(self, str):
			

