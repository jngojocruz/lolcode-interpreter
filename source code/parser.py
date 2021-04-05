'''
CMSC 124 Project
Design and Implementation of Programming Languages
First Semester A.Y. 2020-2021

by:
    Gojo Cruz, Jamlech Iram N.
    Ramos, John Mel R.
'''

from lexer import *
from lex_types import *


i = 0 # global index

### Grammars:

'''	PROGRAM:
    <program> ::= <comment> HAI <linebreak> <code_block> <linebreak> KTHXBYE <comment>
'''
def program(token):
    global i

    i = 0       ## Resets the global variable i every time a new program is feed through the interpreter

    if token[i].lex_type == KEY_COMMENT or token[i].lex_type == MULTICOMMENT_START:
        while token[i].lex_type == KEY_COMMENT or token[i].lex_type == MULTICOMMENT_START:
            comment(token)

    if token[i].lex_type == START_PROGRAM and (token[i-1].lex_type != None and token[i-1].lex_type == NEWLINE):
        print("Entered Start of Program: " + token[i].lexeme)
        kw1 = token[i].lexeme
        i+=1

        code_block_list = []
        op1 = code_block(token, code_block_list)

        if token[i].lex_type == END_PROGRAM and token[i+1].lex_type == NEWLINE:
            print("Entered End of Program: " + token[i].lexeme)
            kw2 = token[i].lexeme
            i+=2

            while i < len(token):
                if token[i].lex_type == KEY_COMMENT or token[i].lex_type == MULTICOMMENT_START:
                    comment(token)
                else:
                    error_prompt()

            return kw1, op1, kw2

        else:
            error_prompt() # no end statement

    else:
        error_prompt() # no start statement


'''	COMMENT:
    <comment> ::= BTW string | <linebreak> OBTW string TLDR <linebreak>
'''
def comment(token):
    global i

    linebreak(token)

    # used for linebreak limit
    token_len = len(token)

    if i < token_len:

        if token[i].lex_type == KEY_COMMENT:
            print("Entered Keyword Comment: " + token[i].lexeme)
            i+=1
            
            if token[i].lex_type == COMMENT_LIT:
                print("Entered Comment Literal: " + token[i].lexeme)
                i+=1

                linebreak(token)

        elif token[i].lex_type == MULTICOMMENT_START and token[i-1].lex_type == NEWLINE:
            print("Entered Multiline Comment start: " + token[i].lexeme)
            i+=1

            linebreak(token)

            if token[i].lex_type == COMMENT_LIT:

                while i < token_len and token[i].lex_type == COMMENT_LIT:
                    print("Entered Comment Literal: " + token[i].lexeme)
                    i+=1

                    linebreak(token)

                if token[i].lex_type == MULTICOMMENT_END and token[i+1].lex_type == NEWLINE:
                    print("Entered Multiline Comment end: " + token[i].lexeme)
                    i+=1

                    linebreak(token)

                else:
                    error_prompt() # no end comment statement

            else:
                error_prompt() # not comment literal

        else:
            error_prompt() # not a comment/no start comment


'''	CODE BLOCK:
    <code_block>	::= <code_block2> <code_block>
    <code_block2>	::= <print> | <declaration> | <comment> | <concat> | <input> |
                        <exp_it> | <assignment> | <if> | <switch>
'''
def code_block(token, code_block_list):
    op1 = code_block2(token)
    if op1 is not None: code_block_list.append(op1)

    while token[i].lex_type != END_PROGRAM:
        code_block(token, code_block_list)

    if len(code_block_list) > 1:
        return tuple(code_block_list)
    else: 
        return code_block_list[0] #changed

def code_block2(token):
    global i
    print("Entered code_block " + token[i].lexeme)

    if token[i].lex_type == PRINT:
        kw1 = token[i].lexeme
        i+=1
        op1 = print_(token)
        return kw1, (op1)

    elif token[i].lex_type == VAR_DEC:
        kw1 = token[i].lexeme
        i+=1
        op1 = declaration(token)
        return kw1, (op1)

    elif token[i].lex_type == KEY_COMMENT or token[i].lex_type == MULTICOMMENT_START:
        comment(token)

    elif token[i].lex_type == CONCAT:
        kw1 = token[i].lexeme
        i+=1
        op1 = concat(token)
        return kw1, (op1)

    elif token[i].lex_type == SCAN:
        kw1 = token[i].lexeme
        i+=1
        op1 = input_(token)
        return kw1, op1

    elif token[i].lex_type == IF_THEN:
        kw1 = token[i].lexeme
        i+=1
        op1 = if_(token)
        return kw1, (op1)

    elif token[i].lex_type == CASE_START:
        kw1 = token[i].lexeme
        i+=1
        op1 = switch(token)
        return kw1, (op1)

    elif token[i].lex_type == VAR_IDENT:
        op = assignment(token)
        return op

    elif token[i].lex_type in EXPR:
        op1 = expr(token)
        return op1

    elif token[i].lex_type == NEWLINE:
        i+=1

    else:
        print(token[i].lexeme, token[i].lex_type)
        error_prompt()


'''	PRINT:
    <start_print> ::= VISIBLE <inf_print>
    <print> ::= <inf_print> <print>
    <inf_print> ::= varident | <expr> | <literal>
'''
def print_(token):
    global i
    print("Entered print " + token[i].lexeme)

    print_list = []
    op1 = inf_print(token)
    op = str(op1) if type(op1) != tuple else op1
    print_list.append(op)
    
    while token[i].lex_type == VAR_IDENT or token[i].lex_type in LITERAL or (token[i].lex_type in EXPR and token[i-1].lex_type != NEWLINE):
        op1 = inf_print(token)
        print_list.append(op1)
    return print_list[0] if len(print_list) == 1 else tuple(print_list)

def inf_print(token):
    global i
    print("Entered inf_print " + token[i].lexeme)


    if token[i].lex_type == VAR_IDENT:
        print("Entered varident " + token[i].lexeme)
        var = token[i].lexeme
        i+=1
        return var

    elif token[i].lex_type in EXPR:
        op1 = expr(token)
        return op1

    elif token[i].lex_type in LITERAL:
        op1 = literal(token)
        return op1

    else:
        error_prompt()


''' CONCATENATION
    <concat> ::= SMOOSH <str> <strconcat>
    <strconcat> ::= AN <str> |
                    AN <str> <strconcat>
    <str> ::= yarn | varident
'''
def concat(token):
    global i

    op1 = strconcat(token)
    return op1
    

def strconcat(token):
    global i

    op1 = func_str(token)
    if token[i].lex_type == OP_SEP:
        print("Entered operator separator " + token[i].lexeme)
        kw1 = token[i].lexeme
        i+=1
        op2 = strconcat(token)
        return op1, kw1, op2
    else:
        if token[i-2].lex_type == OP_SEP:
            return op1
        else:
            error_prompt()

def func_str(token):
    global i

    if token[i].lex_type == STR_LIT:
        print("Entered literal " + token[i].lexeme)
        op1 = token[i].lexeme.strip('"')

    elif token[i].lex_type == VAR_IDENT:
        print("Entered variable identifier " + token[i].lexeme)
        op1 = token[i].lexeme
        
    else:
        op1 = str(token[i].lexeme)

    i += 1
    return op1


'''	INPUT
    <input> ::= GIMMEH varident
'''
def input_(token):
    global i 

    if token[i].lex_type == VAR_IDENT:
        print("Entered variable identifier " + token[i].lexeme)
        var = token[i].lexeme
    else:
        error_prompt()
    i += 1
    return var


'''	EXPRESSION:
    <expr> ::= <sumdiff> | <and> | <or> | <xor> | <not> | <inf_and> | <inf_or> |
<comparison>
'''
def expr(token):
    global i
    print("Entered expr " + token[i].lexeme)

    if token[i].lex_type in ARITHMETIC:
        return sumdiff(token)

    elif token[i].lex_type == AND_OP:
        kw1 = token[i].lexeme
        i+=1
        op1 = and_(token)
        return kw1, (op1)

    elif token[i].lex_type == OR_OP:
        kw1 = token[i].lexeme
        i+=1
        op1 = or_(token)
        return kw1, (op1)

    elif token[i].lex_type == XOR_OP:
        kw1 = token[i].lexeme
        i+=1
        op1 = xor(token)
        return kw1, (op1)

    elif token[i].lex_type == NOT_OP:
        kw1 = token[i].lexeme
        i+=1
        op1 = not_(token)
        return kw1, (op1)

    elif token[i].lex_type == AND_ARITY:
        kw1 = token[i].lexeme
        i+=1
        op1 = inf_and(token)
        return kw1, (op1)

    elif token[i].lex_type == OR_ARITY:
        kw1 = token[i].lexeme
        i+=1
        op1 = inf_or(token)
        return kw1, (op1)
    elif token[i].lex_type in COMPARISON:
        op = comparison(token)
        return op

    i+=1


'''	LITERAL:
    <literal> ::= numbr | numbar | yarn | troof
'''
def literal(token):
    global i

    if token[i].lex_type == INT_LIT:
        print("Entered int literal " + token[i].lexeme)
    elif token[i].lex_type == FLOAT_LIT:
        print("Entered float literal " + token[i].lexeme)
    elif token[i].lex_type == STR_LIT:
        print("Entered string literal " + token[i].lexeme)
        #token[i].lexeme = token[i].lexeme.strip('"')
    elif token[i].lex_type == BOOL_LIT:
        print("Entered boolean literal " + token[i].lexeme)
    elif token[i].lex_type == TYPE_LIT:
        print("Entered type literal " + token[i].lexeme)
    else:
        error_prompt()
    lit = token[i].lexeme
    i+=1
    return lit


'''	AND:
    <and> ::= BOTH OF <bool_exp> AN <bool_exp>
'''	
def and_(token):
    global i
    print("Entered and_ " + token[i].lexeme)

    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)

        if token[i].lex_type == OP_SEP:
            kw1 = token[i].lexeme
            i+=1

            if token[i].lex_type in BOOL_EXP:
                op2 = bool_exp(token)
                return op1, kw1, op2
            
            else:
                error_prompt(token)

        else:
            error_prompt()

    else:
        error_prompt()


'''	OR:
    <or> ::= EITHER OF <bool_exp> AN <bool_exp>
'''
def or_(token):
    global i
    print("Entered or_ " + token[i].lexeme)

    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)

        if token[i].lex_type == OP_SEP:
            kw1 = token[i].lexeme
            i+=1

            if token[i].lex_type in BOOL_EXP:
                op2 = bool_exp(token)
                return op1, kw1, op2
            
            else:
                error_prompt()

        else:
            error_prompt()

    else:
        error_prompt()


'''	XOR:
    <xor> ::= WON OF <bool_exp> AN <bool_exp>
'''
def xor(token):
    global i
    print("Entered xor " + token[i].lexeme)

    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)

        if token[i].lex_type == OP_SEP:
            kw1 = token[i].lexeme
            i+=1

            if token[i].lex_type in BOOL_EXP:
                op2 = bool_exp(token)
                return op1, kw1, op2

            else:
                error_prompt()

        else:
            error_prompt()

    else:
        error_prompt()


'''	NOT:
    <not> ::= NOT <bool_exp>
'''
def not_(token):
    global i
    print("Entered not_ " + token[i].lexeme)

    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)
        return op1

    else:
        error_prompt()


'''	BOOLEAN VALUES:
    <bool_exp> ::= troof | varident
'''
def bool_exp(token):
    global i

    if token[i].lex_type == BOOL_LIT:
        print("Entered BOOL_LIT: " + token[i].lexeme)
        kw1 = token[i].lexeme
        i+=1
        return kw1

    elif token[i].lex_type == VAR_IDENT:
        print("Entered VAR_IDENT: " + token[i].lexeme)
        var = token[i].lexeme
        i+=1
        return var


'''	DECLARATION:
    <declaration> ::= I HAS A varident | I HAS A varident ITZ <literal>
                      I HAS A varident ITZ varident | I HAS A varident ITZ <expr>
'''
def declaration(token):
    global i
    print("Entered declaration " + token[i].lexeme)

    if token[i].lex_type == VAR_IDENT:
        var1 = token[i].lexeme
        i+=1
        if token[i].lex_type == NEWLINE:
            linebreak(token)
            return var1

        if token[i].lex_type == VAR_ASSIGN:
            kw1 = token[i].lexeme
            i+=1

            if token[i].lex_type in LITERAL:
                lit = literal(token)
                return var1, kw1, lit

            elif token[i].lex_type == VAR_IDENT:
                var2 = token[i].lexeme
                i+=1
                return var1, kw1, var2

            elif token[i].lex_type in EXPR:
                var2 = expr(token)
                return var1, kw1, var2

            else:
                error_prompt()
    
            linebreak(token)


''' IF ELSE
    <if> ::= <exp_it> O RLY? <line_break> YA RLY <code_block> <else_if> OIC
    <else_if> ::= MEBBE <expr> <code_block> <else_if> |
                NO WAI <code_block>
'''
def if_(token):
    global i

    ## ADD : Implementation for line breaks
    if token[i].lex_type == IF_COND:
        kw1 = token[i].lexeme
        i+=1
        stmts = code_block3(token)
        kw2 = else_if(token)
        if kw2 == None:
            error_prompt()
            
        if token[i].lex_type == END_IF:
            kw3 = token[i].lexeme
            i+=1
            print("Entered end of IF/IF-ELSE statement")

            return (kw1, (stmts)), kw2, (kw3)
        else:
            error_prompt()

def else_if(token):
    global i

    if token[i].lex_type == ELIF_COND:
        kw1 = token[i].lexeme
        print("Entered code block " + token[i].lexeme)
        i+=1
        if token[i].lex_type in BOOL_EXP:
            cond = expr(token)
        stmts = code_block3(token)
        kw2 = else_if(token)
        if kw2 != None:
            return kw1, cond, (stmts), kw2
        else:
            return kw1, cond, (stmts)
    elif token[i].lex_type == ELSE_COND:
        kw1 = token[i].lexeme
        print("Entered code block " + token[i].lexeme)
        i+=1
        stmts = code_block3(token)
        return kw1, (stmts)
    elif token[i].lex_type == END_IF:
        pass        ## Goes back to caller function 
    else:
        error_prompt()

def code_block3(token):
    global i

    code_block_list = []
    while token[i].lex_type != ELSE_COND and token[i].lex_type != ELIF_COND and token[i].lex_type != END_IF:
        if token[i].lex_type == NEWLINE:
            i+=1
            continue
        code_block_list.append(code_block2(token))
    
    return tuple(code_block_list)


'''	SWITCH CASE	
    <switch> ::= <exp_it> WTF? <case> OMGWTF? <code_block> OIC
    <case> ::= OMG <literal> |
            OMG <literal> <case>
'''
def switch(token):
    global i

    op1 = case(token)

    ## Default switch/case statement
    if token[i].lex_type == DEF_CASE_COND:
        default_stmt = token[i].lexeme
        i+=1
        stmts = code_block4(token)
        if token[i].lex_type == END_IF:
            kw_end = token[i].lexeme
            i+=1
            print("Entered end of SWITCH/CASE")
            return (op1), (default_stmt, (stmts)), (kw_end)
        else:
            error_prompt()
    ## If the next statement is not the default keyword, error.
    else:
        error_prompt()

def case(token):
    global i

    if token[i].lex_type == CASE_COND:
        print("Entered code_block " + token[i].lexeme)
        kw1 = token[i].lexeme
        i+=1
        if token[i].lex_type in LITERAL:
            print("Entered literal " + token[i].lexeme)
            lit = token[i].lexeme
            i+=1
            stmts = code_block4(token)
            ## Only increments the global counter since statement without breaks are allowed.
            lines = [kw1 , lit, (stmts)]
            if token[i].lex_type == BREAK:
                brk = token[i].lexeme
                print("Entered break")
                i+=1
                lines.append(brk)

            op2 = case(token)
            if op2 is not None:
                lines.append(op2)
            return tuple(lines)
        else:
            error_prompt()
    elif token[i].lex_type == DEF_CASE_COND:
        pass
    else:
        error_prompt()

def code_block4(token):
    global i

    code_block_list = []
    while token[i].lex_type != BREAK and token[i].lex_type != END_IF and token[i].lex_type != CASE_COND and token[i].lex_type != DEF_CASE_COND :
        if token[i].lex_type == NEWLINE:
            i+=1
            continue
        code_block_list.append(code_block2(token))
        
        

    return tuple(code_block_list)


''' ASSIGNMENT 
    <assignment> ::= varident R <literal> |
                    varident R varident |
                    varident R <expr>
'''
def assignment(token):
    global i

    if token[i].lex_type == VAR_IDENT:
        varident = token[i].lexeme
        print("Entered varident " + token[i].lexeme)
        i+=1
        if token[i].lex_type == ASSIGN_OP:
            kw_assign = token[i].lexeme
            print("Entered assignment operator " + token[i].lexeme)
            i+=1
            if token[i].lex_type in EXPR:
                ex = expr(token)
                return kw_assign, (varident, ex)
            elif token[i].lex_type == VAR_IDENT:
                varident2 = token[i].lexeme
                print("Entered varident " + token[i].lexeme)
                i+=1
                return kw_assign, (varident, varident2)
            elif token[i].lex_type in LITERAL:
                lit = literal(token)
                return kw_assign, (varident, lit)
            else:
                error_prompt()

        else:
            error_prompt()

    else:
        error_prompt()


'''	LINE BREAK:
    <linebreak> ::= \n
'''
def linebreak(token):
    global i
    print("Entered linebreak")

    # used for linebreak limit
    token_len = len(token)

    if token[i].lex_type == NEWLINE:
        i+=1

        if i < token_len:
            while token[i].lex_type == NEWLINE:
                i+=1

        return True

    return False


'''	ARITHMETIC:
    <sumdiff> ::= SUM OF <sumdiff> AN <sumdiff> | DIFF OF <sumdiff> AN <sumdiff> | <multdiv>
    <multdiv> ::= PRODUKT OF <multdiv> AN <mutdiv> | QUOSHUNT OF <multdiv> an <multdiv> | MOD OF <multdiv> AN <multdiv> | <value>
'''
def sumdiff(token):
    global i

    if token[i].lex_type == ADD:
        i+=1

        op1 = sumdiff(token)
        
        if token[i].lex_type == OP_SEP:
            i+=1
            op2 = sumdiff(token)
        
            return 'SUM OF', (op1, 'AN', op2)
        else:
            error_prompt()

    elif token[i].lex_type == SUB:
        i+=1
        op1 = sumdiff(token)

        if token[i].lex_type == OP_SEP:
            i+=1
            op2 = sumdiff(token)

            return 'DIFF OF', (op1, 'AN', op2)
        else:
            error_prompt(token)

    else:
        op = multdiv(token)
        return op

def multdiv(token):
    global i
    if token[i].lex_type == MUL:
        i+=1
        op1 = sumdiff(token)

        if token[i].lex_type == OP_SEP:
            i+=1
            op2 = sumdiff(token)

            return 'PRODUKT OF', (op1, 'AN', op2)
        else:
            error_prompt(token)

    elif token[i].lex_type == DIV:
        i+=1
        op1 = sumdiff(token)

        if token[i].lex_type == OP_SEP:
            i+=1
            op2 = sumdiff(token)

            return 'QUOSHUNT OF', (op1, 'AN', op2)
        else:
            error_prompt()

    elif token[i].lex_type == MOD:
        i+=1
        op1 = sumdiff(token)

        if token[i].lex_type == OP_SEP:
            i+=1
            op2 = sumdiff(token)

            return 'MOD OF', (op1, 'AN', op2)
        else:
            error_prompt()
        
    else:
        op = value(token)
        i+=1
        return op

def value(token):
    global i

    if token[i].lex_type == INT_LIT:
        return token[i].lexeme
    elif token[i].lex_type == FLOAT_LIT:
        return token[i].lexeme
    elif token[i].lex_type == VAR_IDENT:
        return token[i].lexeme
    else:
        error_prompt()


'''	INFINITE ARITY AND
    <inf_and> ::= ALL OF <bool_exp> AN <inf_and> |
            <bool_exp> AN <inf_and> |
            <bool_exp>
'''
def inf_and(token):
    global i
    
    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)
        if token[i].lex_type == OP_SEP:
            kw_sep = token[i].lexeme
            print("Entered operator separtor " + token[i].lexeme)
            i+=1
            op2 = inf_and(token)
            return op1, kw_sep, op2
        else:
            return op1
    else:
        error_prompt()

def inf_or(token):
    global i

    if token[i].lex_type in BOOL_EXP:
        op1 = bool_exp(token)
        if token[i].lex_type == OP_SEP:
            kw_sep = token[i].lexeme
            print("Entered operator separtor " + token[i].lexeme)
            i+=1
            op2 = inf_or(token)
            return op1, kw_sep, op2
        else:
            return op1
    else:
        error_prompt()


''' COMPARISON
<comparison> ::= BOTH SAEM <comparison> AN <comparison> |
                BOTH SAEM <comparison> AN <comparison> |
                DIFFRINT <comparison> AN <comparison> | 
                DIFFRINT <comparison> AN <comparison> | <comparison2>
<comparison2> ::= BIGGR OF <comparison2> AN <comparison2> |
                    SMALLR OF <comparison2> AN <comparison2> | <comp_op> 
<comp_op>	::= varident | numbr | numbar
'''

def comparison(token):
    global i

    if token[i].lex_type == EQUAL or token[i].lex_type == NOT_EQUAL:
        kw1 = token[i].lexeme
        print("Entered comparison " + token[i].lexeme)
        i+=1
        op1 = comparison(token)
        if token[i].lex_type == OP_SEP:
            sep = token[i].lexeme
            print("Entered operator separator " + token[i].lexeme)
            i+=1
            op2 = comparison(token)
            return kw1, (op1, sep, op2)
    else:
        return comparison2(token)

def comparison2(token):
    global i

    if token[i].lex_type == GREATER_THAN or token[i].lex_type == LESS_THAN:
        kw1 = token[i].lexeme
        print("Entered comparison " + token[i].lexeme)
        i+=1
        op1 = comparison2(token)
        if token[i].lex_type == OP_SEP:
            sep = token[i].lexeme
            print("Entered operator separator " + token[i].lexeme)
            i+=1
            op2 = comparison2(token)
            return kw1, (op1, sep, op2)

    else:
        return comp_op(token)

def comp_op(token):
    global i

    ret = None
    if token[i].lex_type == VAR_IDENT:
        ret = token[i].lexeme
        print("Entered variable identifier " + token[i].lexeme)
        i+=1
    elif token[i].lex_type == INT_LIT:	## Numbr
        ret = token[i].lexeme
        print("Entered numbr literal " + token[i].lexeme)
        i+=1
    elif token[i].lex_type == FLOAT_LIT: ## numbar.
        ret = token[i].lexeme
        print("Entered numbar literal " + token[i].lexeme)
        i+=1
    else:
        error_prompt()

    return ret



# Error prompt
def error_prompt():
    ## Error in the code results in infinite recusrion/loop.
    ## Added a quit() to resolve this error temporarily that would result in
    ## the program ending at the error.
    print("Error!")
    quit()
    