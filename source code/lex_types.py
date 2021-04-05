'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
	Gojo Cruz, Jamlech Iram N.
	Ramos, John Mel R.
'''

# VARIABLES FOR LEXEME TYPES

START_PROGRAM = "Start of Program"
END_PROGRAM = "End of Program"

KEY_COMMENT = "Keyword Comment"
MULTICOMMENT_START = "Multiline Comment Start"
MULTICOMMENT_END = "Multiline Comment End"
COMMENT_LIT = "Comment Literal"

VAR_DEC = "Variable Declaration"
VAR_ASSIGN = "Variable Assignment"
ASSIGN_OP = "Assignment Operator"

AND_OP = "Keyword AND Operator"
OR_OP = "Keyword OR Operator"
XOR_OP = "Keyword XOR Operator"
NOT_OP = "Keyword NOT Operator"
OR_ARITY = "Keyword Arity OR"
AND_ARITY = "Keyword Arity AND"
OP_SEP = "Keyword Operand Separator"

ADD = "Keyword Addition"
SUB = "Keyword Subtraction"
MUL = "Keyword Multiply"
DIV = "Keyword Divide"
MOD = "Keyword Modulo"

GREATER_THAN = "Keyword Greater Than"
LESS_THAN = "Keyword Less Than"
EQUAL = "Keyword Equal"
NOT_EQUAL = "Keyword Not Equal"

EXPR = [AND_OP, OR_OP, XOR_OP, NOT_OP, OR_ARITY, AND_ARITY,
		ADD, SUB, MUL, DIV, MOD, GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL]

CONCAT = "Keyword Concatenation"
TYPECAST = "Keyword Typecast"
TYPECAST_ASSIGN = "Keyword Typecast Assign"
NEW_TYPE = "Keyword New Type"

PRINT = "Keyword Output"
SCAN = "Keyword Input"

IF_THEN = "Keyword If-Then Condition"
IF_COND = "Keyword If"
ELIF_COND = "Keyword Else If"
ELSE_COND = "Keyword Else"
END_IF = "Keyword End If"

CASE_START = "Keyword Case Condition"
CASE_COND = "Keyword Case"
DEF_CASE_COND = "Keyword Default Case"
BREAK = "Keyword Break Case"

LOOP_START = "Keyword Loop Start"
INC = "Keyword Increment"
DEC = "Keyword Decrement"
LOOP_COND = "Keyword Loop"
LOOP_UNTIL = "Keyword Loop Until"
LOOP_WHILE = "Keyword Loop While"
LOOP_END = "Keyword Loop End"

INT_LIT = "Numbr Literal"
FLOAT_LIT = "Numbar Literal"
STR_LIT = "Yarn Literal"
BOOL_LIT = "Troof Literal"
TYPE_LIT = "Type Literal"

VAR_IDENT = "Variable Identifier"

NEWLINE = "Line Break"

EXPR = [AND_OP, OR_OP, XOR_OP, NOT_OP, OR_ARITY, AND_ARITY,
		ADD, SUB, MUL, DIV, MOD, GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL]

COMPARISON = [GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL]

LITERAL = [INT_LIT, FLOAT_LIT, STR_LIT, BOOL_LIT, TYPE_LIT]

VALUE = [INT_LIT, FLOAT_LIT, VAR_IDENT]

STR = [STR_LIT, VAR_IDENT]

ARITHMETIC = [ADD, SUB, MUL, DIV, MOD]

BOOL_EXP = [AND_OP, OR_OP, XOR_OP, NOT_OP, BOOL_LIT, VAR_IDENT]
