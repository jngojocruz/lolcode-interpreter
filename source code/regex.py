'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
	Gojo Cruz, Jamlech Iram N.
	Ramos, John Mel R.
'''

import re

''' ------------ IDENTIFIERS ------------ '''
# Variable Identifier
varident = re.compile("[a-zA-Z]+[_a-zA-Z0-9]*")


''' ------------- LITERALS -------------- '''
# NUMBR Literal
numbr = re.compile("\-?[0-9]+")

# NUMBAR Literal
numbar = re.compile("\-?[0-9]+\.[0-9]+")

# YARN Literal
yarn = re.compile("\"[^\"]*\"")

# TROOF Literal
troof = re.compile("(WIN|FAIL)")

# TYPE Literal
type_literal = re.compile("(NOOB|NUMBR|NUMBAR|YARN|TROOF)")


list_literals = [numbr, numbar, yarn, troof, type_literal]

''' ------------- KEYWORDS ------------- '''
HAI = re.compile("^HAI")
KTHXBYE = re.compile("KTHXBYE$")

# Comments
BTW = re.compile("BTW")
OBTW = re.compile("^OBTW")
TLDR = re.compile("TLDR$")

# Declaration and Assignment
I_HAS_A = re.compile("I HAS A")
ITZ = re.compile("ITZ")
R = re.compile("R")

# Math
AN = re.compile("AN")
SUM_OF = re.compile("SUM OF")
DIFF_OF = re.compile("DIFF OF")
PRODUKT_OF = re.compile("PRODUKT OF")
QUOSHUNT_OF = re.compile("QUOSHUNT OF")
MOD_OF = re.compile("MOD OF")
BIGGR_OF = re.compile("BIGGR OF")
SMALLR_OF = re.compile("SMALLR OF")

# Boolean
BOTH_OF = re.compile("BOTH OF")
EITHER_OF = re.compile("EITHER OF")
WON_OF = re.compile("WON OF")
NOT = re.compile("NOT")
ANY_OF = re.compile("ANY OF")
ALL_OF = re.compile("ALL OF")

# Comparison
BOTH_SAEM = re.compile("BOTH SAEM")
DIFFRINT = re.compile("DIFFRINT")

# Concatenation
SMOOSH = re.compile("SMOOSH")

# Casting
MAEK = re.compile("MAEK")
A = re.compile("A")
IS_NOW_A = re.compile("IS NOW A")

# Input/Output
VISIBLE = re.compile("VISIBLE")
GIMMEH = re.compile("GIMMEH")

# Conditionals: If-Then
O_RLY = re.compile("O RLY\\?")
YA_RLY = re.compile("YA RLY")
MEBBE = re.compile("MEBBE")
NO_WAI = re.compile("NO WAI")
OIC = re.compile("OIC")

# Conditionals: Case
WTF = re.compile("WTF\\?")
OMG = re.compile("OMG")
OMGWTF = re.compile("OMGWTF")
GTFO = re.compile("GTFO")

# Loops
IM_IN_YR = re.compile("IM IN YR")
UPPIN = re.compile("UPPIN")
NERFIN = re.compile("NERFIN")
YR = re.compile("YR")
TIL = re.compile("TIL\n")
WILE = re.compile("WILE")
IM_OUTTA_YR = re.compile("IM OUTTA YR")

list_keywords = [HAI, KTHXBYE, BTW, OBTW, TLDR, I_HAS_A, ITZ, R, 
SUM_OF, DIFF_OF, PRODUKT_OF, QUOSHUNT_OF, MOD_OF, BIGGR_OF, SMALLR_OF,
BOTH_OF, EITHER_OF, WON_OF, NOT, ANY_OF, ALL_OF, BOTH_SAEM, DIFFRINT, SMOOSH,
MAEK, A, IS_NOW_A, VISIBLE, GIMMEH, O_RLY, YA_RLY, MEBBE, NO_WAI, OIC,
WTF, OMG, OMGWTF, IM_IN_YR, UPPIN, NERFIN, YR, TIL, WILE, IM_OUTTA_YR]