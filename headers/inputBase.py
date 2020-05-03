#!bin/python3
# -*- coding: utf-8 -*-
# authors @Flexiboy

from abc import ABC, abstractmethod

class InputBase:

	def __init__(self, inp):
		if isinstance(inp, 'str'):
			self.inp = inp
		elif isinstance(inp, 'list'):
			self.inp = inp

	def __str__(self):
		if isinstance(self.inp, 'str'):
			return self.inp
		else:
			rtrn = ''
			for i in self.inp:
				rtrn += i
			return rtrn

	def __setitem__(self, index, value):
		if isinstance(self.inp, 'list'):
			for i in range(len(self.inp)):
				if i == index:
					self.inp[i] = str(value)

	def __getitem__(self, index):
		if isinstance(self.inp, 'list'):
			if index in range(len(self.inp)):
				return self.inp[index]
			else:
				return 'index out of range'
		else:
			return 'not an array'

	def execute(self):
		pass		
