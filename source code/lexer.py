'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
	Gojo Cruz, Jamlech Iram N.
	Ramos, John Mel R.
'''

import re
from regex import *
from lex_types import *

## The Token class will be the object type responsible for storing the tokens that we got from the lexer.
class Token:
	def __init__(self, lexeme, lex_type):
		self.lexeme = lexeme
		self.lex_type = lex_type

## Lexer Class:
##	This class contains the functions necessary for deconstructing the lol code into lexemes.
class Lexer:
	##	Constructor function for the lexer class
	def __init__(self, source_code):
		self.source_code = source_code

	## Function for opening the given file
	def open_file(self):
		file = open(self.source_code, "r")
		return file

	def make_tokens(self):
		token_list = list()

		lol_file = self.open_file()

		comment_flag = 0
		newline_flag = 0

		## Iterates the file per line
		for line in lol_file:
			## Iterates over each line
			lex = line.strip()

			if comment_flag == 1:
				comment_flag = 0
			
			while len(lex) != 0:
				lex = lex.strip()		### Removes leading and trailing whitespaces
				r_match = None			### Initialize variable
				# print(lex)


## REGEX matching:

				## Code Wrapper
				if HAI.match(lex):
					token = Token("HAI", START_PROGRAM)
					r_match = HAI.match(lex)
					newline_flag = 1

				elif KTHXBYE.match(lex):
					token = Token("KTHXBYE", END_PROGRAM)
					r_match = KTHXBYE.match(lex)
					newline_flag = 1

				## Comments
				elif (not TLDR.match(lex) and comment_flag == 2) or (comment_flag == 1):
					r_match = re.match('.*', lex)
					token = Token(r_match.group(), COMMENT_LIT)
					newline_flag = 1

				elif BTW.match(lex):
					r_match = BTW.match(lex)
					token = Token("BTW", KEY_COMMENT)
					comment_flag = 1
					newline_flag = 1

				elif OBTW.match(lex):
					r_match = OBTW.match(lex)	
					token = Token("OBTW", MULTICOMMENT_START)
					comment_flag = 2
					newline_flag = 1

				elif TLDR.match(lex):
					r_match = TLDR.match(lex)
					token = Token("TLDR", MULTICOMMENT_END)
					comment_flag = 0
					newline_flag = 1

				## Variable Declaration and Assignment
				elif I_HAS_A.match(lex):
					token = Token("I HAS A", VAR_DEC)
					r_match = I_HAS_A.match(lex)
					newline_flag = 1

				elif ITZ.match(lex):
					token = Token("ITZ", VAR_ASSIGN)
					r_match = ITZ.match(lex)

				elif R.match(lex):
					token = Token("R", ASSIGN_OP)
					r_match = R.match(lex)

				## Boolean operator
				elif BOTH_OF.match(lex):
					r_match = BOTH_OF.match(lex)
					token = Token("BOTH OF", AND_OP)

				elif EITHER_OF.match(lex):
					r_match = EITHER_OF.match(lex)
					token = Token("EITHER OF", OR_OP)

				elif WON_OF.match(lex):
					r_match = WON_OF.match(lex)
					token = Token("WON OF", XOR_OP)

				elif NOT.match(lex):
					r_match = NOT.match(lex)
					token = Token("NOT", NOT_OP)

				elif ANY_OF.match(lex):
					r_match = ANY_OF.match(lex)
					token = Token("ANY OF", OR_ARITY)

				elif ALL_OF.match(lex):
					r_match = ALL_OF.match(lex)
					token = Token("ALL OF", AND_ARITY)

				## Arithmetic Operators
				elif AN.match(lex):
					token = Token("AN", OP_SEP)
					r_match = AN.match(lex)

				elif SUM_OF.match(lex):
					token = Token("SUM OF", ADD)
					r_match = SUM_OF.match(lex)

				elif DIFF_OF.match(lex):
					token = Token("DIFF OF", SUB)
					r_match = DIFF_OF.match(lex)

				elif PRODUKT_OF.match(lex):
					r_match = PRODUKT_OF.match(lex)
					token = Token("PRODUKT OF", MUL)

				elif QUOSHUNT_OF.match(lex):
					r_match = QUOSHUNT_OF.match(lex)
					token = Token("QUOSHUNT OF", DIV)

				elif MOD_OF.match(lex):
					r_match = MOD_OF.match(lex)
					token = Token("MOD OF", MOD)

				elif BIGGR_OF.match(lex):
					r_match = BIGGR_OF.match(lex)
					token = Token("BIGGR OF", GREATER_THAN)

				elif SMALLR_OF.match(lex):
					r_match = SMALLR_OF.match(lex)
					token = Token("SMALLR OF", LESS_THAN)

				## Comparison
				elif BOTH_SAEM.match(lex):
					r_match = BOTH_SAEM.match(lex)
					token = Token("BOTH SAEM", EQUAL)

				elif DIFFRINT.match(lex):
					r_match = DIFFRINT.match(lex)
					token = Token("DIFFRINT", NOT_EQUAL)

				## Concatenaton
				elif SMOOSH.match(lex):
					r_match = SMOOSH.match(lex)
					token = Token("SMOOSH", CONCAT)

				## Casting
				elif MAEK.match(lex):
					r_match = MAEK.match(lex)
					token = Token("MAEK", TYPECAST)

				elif A.match(lex):
					r_match = A.match(lex)
					token = Token("A", TYPECAST_ASSIGN)

				elif IS_NOW_A.match(lex):
					r_match = IS_NOW_A.match(lex)
					token = Token(lex, NEW_TYPE)

				## Input/Output
				elif VISIBLE.match(lex):
					r_match = VISIBLE.match(lex)
					token = Token("VISIBLE", PRINT)
					newline_flag = 1

				elif GIMMEH.match(lex):
					r_match = GIMMEH.match(lex)
					token = Token("GIMMEH", SCAN)

				## Conditionals: If-Then
				elif O_RLY.match(lex):
					r_match = O_RLY.match(lex)
					token = Token("O RLY?", IF_THEN)

				elif YA_RLY.match(lex):
					r_match = YA_RLY.match(lex)
					token = Token("YA RLY", IF_COND)

				elif MEBBE.match(lex):
					r_match = MEBBE.match(lex)
					token = Token("MEBBE", ELIF_COND)

				elif NO_WAI.match(lex):
					r_match = NO_WAI.match(lex)
					token = Token("NO WAI", ELSE_COND)

				elif OIC.match(lex):
					r_match = OIC.match(lex)
					token = Token("OIC", END_IF)

				## Conditionals: Case
				elif WTF.match(lex):
					r_match = WTF.match(lex)
					token = Token("WTF?", CASE_START)

				elif OMGWTF.match(lex):
					r_match = OMGWTF.match(lex)
					token = Token("OMGWTF", DEF_CASE_COND)

				elif OMG.match(lex):
					r_match = OMG.match(lex)
					token = Token("OMG", CASE_COND)

				elif GTFO.match(lex):
					r_match = GTFO.match(lex)
					token = Token("GTFO", BREAK)

				## Loops
				elif IM_IN_YR.match(lex):
					r_match = IM_IN_YR.match(lex)
					token = Token("IM IN YR", LOOP_START)

				elif UPPIN.match(lex):
					r_match = UPPIN.match(lex)
					token = Token("UPPIN", INC)

				elif NERFIN.match(lex):
					r_match = NERFIN.match(lex)
					token = Token("NERFIN", DEC)

				elif YR.match(lex):
					r_match = YR.match(lex)
					token = Token("YR", LOOP_COND)

				elif TIL.match(lex):
					r_match = TIL.match(lex)
					token = Token("TIL", LOOP_UNTIL)

				elif WILE.match(lex):
					r_match = WILE.match(lex)
					token = Token("WILE", LOOP_WHILE)

				elif IM_OUTTA_YR.match(lex):
					r_match = IM_OUTTA_YR.match(lex)
					token = Token("IM OUTTA YR", LOOP_END)
				
				## Literal
				elif numbar.match(lex):
					r_match = numbar.match(lex)
					token = Token(r_match.group(), FLOAT_LIT)

				elif numbr.match(lex):
					r_match = numbr.match(lex)
					token = Token(r_match.group(), INT_LIT)

				elif yarn.match(lex):
					r_match = yarn.match(lex)
					token = Token(r_match.group(), STR_LIT)
					
				elif troof.match(lex):
					r_match = troof.match(lex)
					token = Token(r_match.group(), BOOL_LIT)

				elif type_literal.match(lex):
					r_match = type_literal.match(lex)
					token = Token(r_match.group(), TYPE_LIT)
				
				## Variable Identifier
				elif varident.match(lex):
					r_match = varident.match(lex)
					token = Token(r_match.group() ,VAR_IDENT)

				## Possibly for comment string
				elif re.match('.*', lex):
					r_match = re.match('.*', lex)
					token = Token(r_match.group(), COMMENT_LIT)


				token_list.append(token)

				span = r_match.span()
				lex = lex[span[1]:]		## Removes the string that is matched from the curernt line


			## New Line
			## will only be called if necessary
			## not totally considered on tokens
			if newline_flag == 1:
				token = Token(r"\n", NEWLINE)
				token_list.append(token)
				newline_flag = 0


		return token_list