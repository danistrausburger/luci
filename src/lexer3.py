from ply.lex import lex
from ply.yacc import yacc
import sys

# --- Tokenizer
kwords = {
    'if' : 'IF',
    'elif' : 'ELIF',
    'el' : 'EL',
    'scene' : 'SCENE',
    'from' : 'FROM',
    'to' : 'TO',
    'deal' : 'DEAL',
    'ex' : 'EX',
    'action' : 'ACTION',
    'cut' : 'CUT',
    'create' : 'CREATE',
    'tartarus' : 'TARTARUS',
    'truth' : 'TRUTH',
    'lie' : 'LIE',
    'die' : 'DIE',
    'retaliate' : 'RETALIATE',
    'gate' : 'GATE'
}

# Token Types
tokens = ('EOF', 'INCR', 'DECR', 'ADD', 'SUB', 'MULT', 'DIV', 
          'GREQUAL', 'LEQUAL', 'ISNOT', 'ASSIGN', 'GREATER', 'LESS', 'EQUALS', 
          'NOT', 'AND', 'OR', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
          'CHARCHAR', 'NUMBER') + tuple(kwords.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_EOF = r'EOF'
t_INCR = r'\+\+'
t_DECR = r'\-\-'
# t_ADDEQ = r'\+='
# t_SUBEQ = r'\-='
# t_MULTEQ = r'\*='
# t_DIVEQ = r'/='
t_ADD = r'\+'
t_SUB = r'-'  
t_MULT = r'\*'
t_DIV = r'/'
t_GREQUAL = r'>='
t_LEQUAL = r'<='
t_ISNOT = r'~='
t_ASSIGN = r'\<-'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUALS = r'=\?'
t_NOT = r'~'
t_AND = r'&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# HEY CHAR Rule for variable CHARCHARs
def t_CHARCHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = kwords.get(t.value, 'CHARCHAR') # Checks for key words, otherwise Char Char
    return t

# Number Rule
def t_NUMBER(t):
    r'\d+(\.\d+)?' # 1 or more digits/floats
    # if '.' not in t.value:
    #     t.value = int(t.value)
    # else:
    #     t.value = float(t.value)
    t.value = float(t.value)
    return t

def t_ignore_comment(t):
    r'\#.*'

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

def p_statement_if(p):
    '''
    statement : IF LPAREN expression RPAREN ACTION statement CUT
             | IF LPAREN expression RPAREN ACTION statement CUT EL ACTION statement CUT
    '''
    if len(p) == 8:  # Only if, without else
        p[0] = ('if:', p[3], p[6])
    else:  # if with else
        p[0] = ('if_el:', p[3], p[6], p[10])

def p_statement_expr(p):
    '''
    statement : expression
    '''
    p[0] = p[1]

def p_expression_binop(p):
    '''
    expression : expression ADD expression
               | expression SUB expression
               | expression MULT expression
               | expression DIV expression
               | expression INCR
               | expression DECR
    '''
    if p[2] == '+':
        p[0] = ('binop', '+', p[1], p[3])
    elif p[2] == '-':
        p[0] = ('binop', '-', p[1], p[3])
    elif p[2] == '*':
        p[0] = ('binop', '*', p[1], p[3])
    elif p[2] == '/':
        p[0] = ('binop', '/', p[1], p[3])
    elif p[2] == '++':
        p[0] = ('unary', '++', p[1])
    elif p[2] == '--':
        p[0] = ('unary', '--', p[1])

def p_expression_comparison(p):
    '''
    expression : expression LESS expression
               | expression GREATER expression
               | expression LEQUAL expression
               | expression GREQUAL expression
               | expression EQUALS expression
               | expression ISNOT expression
    '''
    if p[2] == '<':
        p[0] = ('comparison', '<', p[1], p[3])
    elif p[2] == '>':
        p[0] = ('comparison', '>', p[1], p[3])
    elif p[2] == '<=':
        p[0] = ('comparison', '<=', p[1], p[3])
    elif p[2] == '>=':
        p[0] = ('comparison', '>=', p[1], p[3])
    elif p[2] == '=?':
        p[0] = ('comparison', '=?', p[1], p[3])
    elif p[2] == '~=':
        p[0] = ('comparison', '~=', p[1], p[3])

def p_expression_assign(p):
    '''
    expression : CHARCHAR ASSIGN expression
    '''
    p[0] = ('assignment', p[1], p[3])

def p_expression(p):
    '''
    expression : term
               | expression ADD term
               | expression SUB term
               | expression MULT term
               | expression DIV term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = ('binop', '+', p[1], p[3])
        elif p[2] == '-':
            p[0] = ('binop', '-', p[1], p[3])
        elif p[2] == '*':
            p[0] = ('binop', '*', p[1], p[3])
        elif p[2] == '/':
            p[0] = ('binop', '/', p[1], p[3])

def p_term(p):
    '''
    term : factor
         | term MULT factor
         | term DIV factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = ('binop', '*', p[1], p[3])
    elif p[2] == '/':
        p[0] = ('binop', '/', p[1], p[3])

def p_factor(p):
    '''
    factor : NUMBER
           | CHARCHAR
           | LPAREN expression RPAREN
           | ADD factor
           | SUB factor
    '''
    if len(p) == 2:
        if isinstance(p[1], float):
            p[0] = ('number', p[1])
        else:
            p[0] = ('CHARCHAR', p[1])
    elif p[1] == '(':
        p[0] = ('grouped', p[2])
    elif p[1] == '+':
        p[0] = ('unary', '+', p[2])
    elif p[1] == '-':
        p[0] = ('unary', '-', p[2])

def p_error(p):
    print(f'Syntax error at {p.value!r}')

# Build the parser
parser = yacc()

# Parse an expression
# ast = parser.parse('2 * 3 + 4 * (5 - x)')
# print(ast)

while True:
    try:
        s = input('expr > ')
    except EOFError:
        break
    if not s:
        continue
    ast = parser.parse(s)
    print(ast)