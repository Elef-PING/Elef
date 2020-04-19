#!/bin/python3
# -*- coding: utf-8 -*-
@authors @Flexiboy

from random import choice

class WatchOut:

	def __init__(self, lang, path):
		self.string = ''
		with open(path, 'r') as inp:
			array = []
			for i in len(inp):
				array.append(i)

			watchout = choice(array)
			self.string = inp[watchout]

	def __str__(self):
		return self.string
