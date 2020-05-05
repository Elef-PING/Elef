#!bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

from abc import ABC, abstractmethod
from input import *

APP_PATH = ../files/application_keywords.xml
ACT_PATH = ../files/action_keywords.xml
TIM_PATH = ../files/time_keywords.xml
LANG = configure.getLang()

class Parser(Input):

	def __init__(self, inp):
		self.input = inp
		self.application_keywords = []
		self.action_keywords = []
		self.time_keywords = []
		
		tmp = []
		with open(APP_PATH, "r") as keywordsfile:
			for i in keywordsfile:
				index1, index2 = i.find("kw"), i.find("lang")
				if index2 == -1 AND index1 != -1:
					tmp.append(i.split("\"")[1])
				elif index1 == -1 AND index2 != -1:
					if i[12:13] == LANG:
						tmp.append(i.split(">")[1].split("<")[0])
						self.application_keywords.append(tmp)
						tmp = []
				elif index1 == -1 && index2 == -1:
					print("file error")

		with open(ACT_PATH, "r") as keywordsfile:
			for i in keywordsfile: 
				index1, index2 = i.find("kw"), i.find("lang")
				if index2 == -1 AND index1 != -1:
					tmp.append(i.split("\"")[1]
				elif index1 == -1 AND index2 != -1:
					if i[12:13] == LANG:
						tmp.append(i.split(">")[1].split("<")[0])
						self.action_keywords.append(tmp)
						tmp = []
				elif index1 == -1 && index2 == -1:
					print("file error")

		with open(TIM_PATH, "r") as keywordsfile:
			for i in keywordsfile:
				index1, index2 = i.find("kw"), i.find("lang")
				if index2 == -1 AND index1 != -1:
					tmp.append(i.split("\"")[1]
				elif index1 == -1 AND index2 != -1:
					

		self.parsed = parser(self.input, keywords)


	def evaluate(self):
		if self.parsed is not None:
			return 0
		else:
			return -1

	def parser(self, inp, keywords):
		parsed = None
		if isinstance(self, str):
			
		return parsed
			

