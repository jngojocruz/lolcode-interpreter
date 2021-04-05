'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
	Gojo Cruz, Jamlech Iram N.
	Ramos, John Mel R.
'''

class Symbol_Table:
	def __init__(self):
		self.symbol_table = {}

	def set_table(self, identifier, value):
		self.symbol_table[identifier] = value

	def get_table(self, identifier):
		value = self.symbol_table.get(identifier)
		return value
