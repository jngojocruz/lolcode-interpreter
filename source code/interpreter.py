'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
	Gojo Cruz, Jamlech Iram N.
	Ramos, John Mel R.
'''

from parser import *
from symbol_table import *
from tkinter import * 
from tkinter import filedialog 
import os

symbol_table = Symbol_Table()

class Interpreter:
	def __init__(self, parse_tree):
		self.parse_tree = parse_tree

	## Functions for executing operations, expressions, and statements 

	def assign_op(self, val):
		if val == "WIN":
			return True
		elif val == "FAIL":
			return False

	def get_val(self, op):

		if op is None:
			return "FAIL"
		elif type(op) == tuple:
			val = self.evaluate(op)
			return val if val is not None else "FAIL"
		elif numbar.match(op) or numbr.match(op) or yarn.match(op) or troof.match(op):
			if yarn.match(op):
				op = op.strip('"')
			elif numbar.match(op):
				op = float(op)
			elif numbr.match(op):
				op = int(op)
			return op
		elif varident.match(op):
			val = symbol_table.get_table(op)
			
			if val is not None:
				if val == "NOOB":
					print("Error. Cannot print variable {} has of type 'NOOB'".format(op))
					quit()
				else:
					return val
			else:
				print("Error. Variable {} undeclared".format(op))
				quit()

	## Boolean Operations
	def and_op(self, ast):
		val1 = self.get_val(ast[0])
		val2 = self.get_val(ast[2])
		op1 = self.assign_op(val1)
		op2 = self.assign_op(val2)
		res = op1 and op2
		return "WIN" if res else "FAIL"

	def or_op(self, ast):
		val1 = self.get_val(ast[0])
		val2 = self.get_val(ast[2])
		op1 = self.assign_op(val1)
		op2 = self.assign_op(val2)
		res = op1 or op2
		return "WIN" if res else "FAIL"

	def xor_op(self, ast):
		val1 = self.get_val(ast[0])
		val2 = self.get_val(ast[2])
		op1 = self.assign_op(val1)
		op2 = self.assign_op(val2)
		res = (op1 != op2)
		return "WIN" if res else "FAIL"

	def not_op(self, ast):
		val = self.get_val(ast)
		op1 = self.assign_op(val)
		res = not op1
		return "WIN" if res else "FAIL"

	## Declaration
	def declare_op(self, ast):
		if type(ast) == tuple and len(ast) > 1:
			var = ast[0]
			val = self.get_val(ast[2])
		else:
			var = ast
			val = "NOOB"
		symbol_table.set_table(var, val)
		update_table_ui(symbol_table.symbol_table)
		return var, symbol_table.get_table(var)

	## Input
	def input_op(self, ast):
		if ast in symbol_table.symbol_table.keys():
			val = input()
			symbol_table.set_table(ast, val)
			update_table_ui(symbol_table.symbol_table)
		else:
			print("Error. Variable {} undeclared".format(ast))
			quit()

	## Concatenation
	def concat_op(self, ast):
		if type(ast) != tuple:
			return ast
		else:
			return ast[0] + self.concat_op(ast[2])

	## Printing
	def print_op(self, ast):
		val = None

		if type(ast) == tuple:
			#print(ast)					
			if len(ast) == 2 and type(ast[1]) == tuple:
				val = self.get_val(ast)
			else:
				val = ""
				for i in ast:
					#print(i)
					op = self.get_val(i)				
					val = val + str(op)
		else:
			val = self.get_val(ast)
		print(val)
		exec_area.insert(END, str(val) + "\n")
		
		
	## Arithmetic Function
	def eval_add(self, op):
		op1 = self.evaluate(op[0])
		op2 = self.evaluate(op[2])
		return op1 + op2

	def eval_sub(self, op):
		op1 = self.evaluate(op[0])
		op2 = self.evaluate(op[2])
		return op1 - op2 
		
	def eval_product(self, op):
		op1 = self.evaluate(op[0])
		op2 = self.evaluate(op[2])
		return op1 * op2

	def eval_div(self, op):
		op1 = self.evaluate(op[0])
		op2 = self.evaluate(op[2])
		if type(op1) == int and type(op2) == int:
			return op1 // op2
		else:
			return op1 / op2

	def eval_modulo(self, op):
		op1 = self.evaluate(op[0])
		op2 = self.evaluate(op[2])
		return op1%op2

	## IF-Then statement functions
	def if_then(self, ast):
		done = False		## Keeps track if the following else-if/else statements should be executed.
		for block in ast:
			if YA_RLY.match(block[0]) and symbol_table.get_table("IT") == "WIN":
				for line in block[1]:
					self.evaluate(line)
				done = True		## This means that the following condition should not be executed anymore
			elif MEBBE.match(block[0]) and not done:
				## Evaluate Condition
				self.evaluate(block[1])		## Condition Statement
				## If the resulting evaluation of the conditional statement results in a WIN, executes the line of code
				if symbol_table.get_table("IT") == "WIN":
					for line in block[1]:
						self.evaluate(line)
					done = True
			elif NO_WAI.match(block[0]) and not done:
				for line in block[1]:
					self.evaluate(line)
			elif type(block) != tuple:
				if OIC.match(block):
					pass		## End of if/else block

	def switch_case(self, ast, brk, cond):
		omg = ast[0]							## Case statements
		brk = self.case_clause(omg, brk, cond)		## After executing OMG statements, proceeds to OMGWTF clauses
		if brk == None:
			brk = False
		omgwtf = ast[1]
		self.def_clause(omgwtf, brk, cond)		## Default clause

		kw_oic = ast[2]							## End switch/case			


	def case_clause(self, ast, brk, cond):
		kw_omg = ast[0]							## OMG Keyword

		lit = self.evaluate(ast[1])				## Literal

		if lit == symbol_table.get_table("IT"):
			for line in ast[2]:
				self.evaluate(line)

			if type(ast[3]) != tuple and GTFO.match(ast[3]):	## GTFO (break) keyword exist
				brk = True
				return True
			else:												## The switch case will continue
				try:											## If there is no break statement, calls the next subtree of the switch/case parse tree.
					self.case_clause(ast[3], False, True)
				except:
					pass	
				
		elif cond == True and brk == False:
			for line in ast[2]:
				self.evaluate(line)

			if type(ast[3]) != tuple and GTFO.match(ast[3]):	## GTFO (break) keyword exist
				brk = True
				return True
			else:												## The switch case will continue
				try:
					self.case_clause(ast[3], False, True)
				except:
					pass

		else:
			try:
				if type(ast[3]) != tuple and GTFO.match(ast[3]):			## The third index contains a GTFO keyword
					try:
						self.case_clause(ast[4], False, False)				## The next case clause is most likely in the next index
					except(IndexError):
						return False
				else:										
					self.case_clause(ast[3], False, False)				
			except(IndexError):
				return False														## Last index

	def def_clause(self, ast, brk, cond):
		if brk == False:
			kw_omgwft = ast[0]
			
			for line in ast[1]:
				self.evaluate(line)

	# Infinite AND
	def inf_and_arity(self, ast):
		op1 = self.assign_op(ast[0])

		if type(ast[2]) != tuple:
			op2 = self.assign_op(ast[2])
		else:
			op2 = self.inf_and_arity(ast[2])

		return op1 and op2

	# Infinite OR
	def inf_or_arity(self, ast):
		op1 = self.assign_op(ast[0])

		if type(ast[2]) != tuple:
			op2 = self.assign_op(ast[2])
		else:
			op2 = self.inf_or_arity(ast[2])
	
		return op1 or op2

	## Assignment Statements	
	## ast[0] - Destination
	## ast[1] - Location
	## Check in the symbol table first if the variable already exist. If not, must return an error (Variable not initialized)
	def assignment_stmnt(self, ast):
		if ast[0] in symbol_table.symbol_table.keys():				## If the variable identifier is already in the symbol table (initialized)
			symbol_table.set_table(ast[0], self.evaluate(ast[1]))
			update_table_ui(symbol_table.symbol_table)
		else:
			print("Error. Variable {} uninitialized!".format(ast[0]))
			quit()

	## Comparison functions
	def equal_to(self, ast):
		op1 = self.evaluate(ast[0])
		op2 = self.evaluate(ast[2])

		return "WIN" if op1 == op2 else "FAIL"

	def not_equal_to(self, ast):
		op1 = self.evaluate(ast[0])
		op2 = self.evaluate(ast[2])
			
		return "WIN" if op1 != op2 else "FAIL"

	def greater_than_op(self, ast):
		op1 = self.evaluate(ast[0])
		op2 = self.evaluate(ast[2])
			
		return op1 if op1 > op2 else op2

	def less_than_op(self, ast):
		op1 = self.evaluate(ast[0])
		op2 = self.evaluate(ast[2])
			
		return op1 if op1 < op2 else op2

	def interpret(self):
		ast = self.parse_tree
		pos = 0
		if type(ast[1][0]) != tuple and len(ast[1]) == 2:
			val = self.evaluate(ast[1])
		else:
			while pos < len(ast[1]):
				val = self.evaluate(ast[1][pos])
				# print(val)
				pos+=1


	# Function that will determine the current token to be evaluated
	def evaluate(self, ast):
		# check first keyword/varident of a line
		# ast is now pointing on code blocks

		if ast != None:

			if type(ast) != tuple:
				if numbar.match(ast):
					return float(ast)

				elif numbr.match(ast):
					return int(ast)

				elif yarn.match(ast):
					return ast.strip('"')

				elif troof.match(ast):
					return ast

				elif varident.match(ast):
					if ast in symbol_table.symbol_table.keys():
						return symbol_table.get_table(ast)
			
			# and
			elif BOTH_OF.match(ast[0]):
				val = self.and_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			# or
			elif EITHER_OF.match(ast[0]):
				val = self.or_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			# xor
			elif WON_OF.match(ast[0]):
				val = self.xor_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			# not
			elif NOT.match(ast[0]):
				val = self.not_op(ast[1])
				symbol_table.set_table("IT", val)
				return symbol_table.get_table("IT")

			# infinite and
			elif ALL_OF.match(ast[0]):
				val = self.inf_and_arity(ast[1])
				symbol_table.set_table("IT", "WIN") if val else symbol_table.set_table("IT", "FAIL")
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			# infinite or
			elif ANY_OF.match(ast[0]):
				val = self.inf_or_arity(ast[1])
				symbol_table.set_table("IT", "WIN") if val else symbol_table.set_table("IT", "FAIL")
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			# declaration
			elif I_HAS_A.match(ast[0]):
				val = self.declare_op(ast[1])
				return val

			# input
			elif GIMMEH.match(ast[0]):
				self.input_op(ast[1])

			# concat
			elif SMOOSH.match(ast[0]):
				val = self.concat_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				print(val)

			# print
			elif VISIBLE.match(ast[0]):
				self.print_op(ast[1])
				
			## IF/Else statements
			elif O_RLY.match(ast[0]):
				self.if_then(ast[1])

			## Switch/Case statement
			elif WTF.match(ast[0]):
				self.switch_case(ast[1], False, False)

			## Assignment Operation
			elif R.match(ast[0]):
				self.assignment_stmnt(ast[1])

			## Arithmetic Operator
			elif SUM_OF.match(ast[0]):
				val = self.eval_add(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif DIFF_OF.match(ast[0]):
				val = self.eval_sub(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif PRODUKT_OF.match(ast[0]):
				val = self.eval_product(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif QUOSHUNT_OF.match(ast[0]):
				val = self.eval_div(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")
			
			elif MOD_OF.match(ast[0]):
				val = self.eval_modulo(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			## Comparison Operator
			elif BOTH_SAEM.match(ast[0]):
				val = self.equal_to(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif DIFFRINT.match(ast[0]):
				val = self.not_equal_to(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif BIGGR_OF.match(ast[0]):
				val = self.greater_than_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")

			elif SMALLR_OF.match(ast[0]):
				val = self.less_than_op(ast[1])
				symbol_table.set_table("IT", val)
				update_table_ui(symbol_table.symbol_table)
				return symbol_table.get_table("IT")


#############################################################################################################				
# GUI

directory = "/home/jngojocruz/Desktop/CMSC124/CMSC124-project-lol FINAL"

def browseFiles(): 
	global directory

	filename = filedialog.askopenfilename(initialdir = directory, 
										  title = "Select a File", 
										  filetypes = (("LOL files", 
														"*.lol"), 
													   ))

	directory = filename            ## Reassign the inital directory to the previous directory selected
	
	if filename != ():        
		code_area.delete("1.0", "end")

		fp = open(filename, 'r')
		contents = fp.read()
		
		dir_area.configure(state = "normal")
		dir_area.delete(0, END)
		dir_area.insert(END, filename)
		dir_area.configure(state = "readonly")

		code_area.insert(END, str(contents))

		lexer = Lexer(filename)
		tokens = lexer.make_tokens()
		for i in tokens:
			print (i.lexeme +"                          "+str(i.lex_type))

		## Clears the current table
		lex_column.delete("1.0", END)
		## Clears the current execution area
		exec_area.delete("1.0", END)

		for tok in tokens:
			if tok.lex_type == NEWLINE:
				continue
			lex_column.insert(END, "{:40} {}\n".format(tok.lexeme, tok.lex_type))
		
		symbol_table.symbol_table = {}			## Clears the previous contents of the symbol table
		symbol_table.set_table("IT", "NOOB")
		ast = program(tokens)
		inter = Interpreter(ast)

		## Clears the terminal
		try:
			os.system("clear")		## For linux system
		except:
			os.system("cls")		## For windows system

		for key in symbol_table.symbol_table:
			print("{} {}".format(key, symbol_table.symbol_table.get(key)))

		update_table_ui(symbol_table.symbol_table)
		inter.interpret()

## Used to update values in the symbol table (GUI)
def update_table_ui(symbol_table):
	table_column.delete("1.0", END)

	for key in symbol_table:
		table_column.insert(END, "{:20} {}\n".format(key, symbol_table.get(key)))



## GUI
root = Tk()
root.title("LOL CODE INTERPRETER")

## Column 1 
file_browser_frame = Frame(root, bg = "blue")
file_browser = Button(file_browser_frame, text = "BROWSE FILES", pady = 7, bg = "black", fg = "white", command = browseFiles)

code_frame = Frame(root)
vert_scrollbar1 = Scrollbar(code_frame, orient = VERTICAL)

dir_area = Entry(file_browser_frame, width = 50, font = ('helvetica', 25), state = "readonly")
code_area = Text(code_frame, yscrollcommand = vert_scrollbar1.set)



## Column 2 & 3
interpreter_column = Label(root, text = "LOL CODE INTERPRETER", bg = "#2b2929", fg = "white", pady = 7)

## Lexemes Column
lex_frame = Frame(root)
	## Scrollbars for the lexemes table
vert_scrollbar = Scrollbar(lex_frame, orient=VERTICAL)
horizontal_scrollbar = Scrollbar(lex_frame, orient=HORIZONTAL)
	## --------------------------------
lex_label = Label(lex_frame, text = "Lexeme", relief = "groove", pady = 3)
classification_label = Label(lex_frame, text = "Classification", relief = "groove", pady = 3)
classification_column = Text(lex_frame, width = 60, borderwidth = 0)
lex_column = Text(lex_frame, width = 60, borderwidth = 0, wrap = "none", yscrollcommand = vert_scrollbar.set, xscrollcommand = horizontal_scrollbar.set)

## Symbol Table Column
table_frame = Frame(root)
	## Scrollbars for the symbol table
vert_scrollbar2 = Scrollbar(table_frame, orient=VERTICAL)
horizontal_scrollbar2 = Scrollbar(table_frame, orient=HORIZONTAL)
	## --------------------------------
ident_label = Label(table_frame, text = "Identifier", relief = "groove", pady = 3)
val_label = Label(table_frame, text = "Value", relief = "groove", pady = 3)
val_column = Text(table_frame, width = 60, borderwidth = 0)
table_column = Text(table_frame, width = 60, borderwidth = 0, wrap = "none", yscrollcommand = vert_scrollbar2.set, xscrollcommand = horizontal_scrollbar2.set)

## EXECUTE Panel
execute = Label(root, text = "Execute", pady = 7, bg = "#2b2929", fg = "white")
exec_area = Text(root)

## Packing elements on the grid
root.grid_columnconfigure(0, weight = 1)

vert_scrollbar1.grid(row = 0, column = 3, rowspan = 2, sticky = "NS")
vert_scrollbar1.config(command=code_area.yview)

file_browser_frame.grid_columnconfigure(0, weight = 1)

file_browser_frame.grid(row = 0, column = 0, sticky = "EW")
dir_area.grid(row = 0, column = 0, sticky = "EW")                            ## Shows the current DIR
file_browser.grid(row = 0, column = 1, sticky = "EW")                        ## Button

code_frame.grid(row = 1, column = 0, sticky = "EW")
code_frame.grid_columnconfigure(0, weight = 1)
code_area.grid(row = 0, column = 0, sticky = "EW")

interpreter_column.grid(row = 0, column = 1, columnspan = 2, sticky = "EW")
## Lexemes
lex_frame.grid(row = 1, column = 1)
lex_label.grid(row = 0, column = 0, sticky = "EW")
classification_label.grid(row = 0, column = 1, sticky = "EW")
lex_column.grid(row = 1, column = 0, columnspan = 2)

vert_scrollbar.grid(column = 3, row = 1, rowspan = 2, sticky = "NS")
horizontal_scrollbar.grid(row = 10, columnspan = 2, sticky = "EW")

vert_scrollbar.config(command=lex_column.yview)
horizontal_scrollbar.config(command=lex_column.xview)
# classification_column.grid(row = 1, column = 1)

lex_frame.grid_columnconfigure(0, weight = 1)	
lex_frame.grid_rowconfigure(0, weight = 1)

## Symbol Table	
table_frame.grid(row = 1, column = 2)
ident_label.grid(row = 0, column = 0, sticky = "EW")
val_label.grid(row = 0, column = 1, sticky = "EW")

table_column.grid(row = 1, column = 0, columnspan = 2, sticky = "EW")
# val_column.grid(row = 1, column = 1)
table_frame.grid_columnconfigure(0, weight = 1)

vert_scrollbar2.grid(column = 3, row = 1, rowspan = 2, sticky = "NS")
horizontal_scrollbar2.grid(row = 10, columnspan = 2, sticky = "EW")

vert_scrollbar2.config(command=table_column.yview)
horizontal_scrollbar2.config(command=table_column.xview)

execute.grid(row = 2, columnspan = 3, sticky = "EW")
exec_area.grid(row = 3, columnspan = 3, sticky = "NEWS")

root.protocol("WM_DELETE_WINDOW", root.quit) #Quits the program if the user presses the X button
root.mainloop()