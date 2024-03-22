from ply.lex import lex, LexToken
import ply.yacc as yacc
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
tokens = ('EOF', 'INCR', 'DECR', 'ADDEQ', 'SUBEQ', 'MULTEQ', 'DIVEQ', 
          'ADD', 'SUB', 'MULT', 'DIV', 'GREQUAL', 'LEQUAL',
          'ISNOT', 'GREATER', 'LESS', 'EQUALS', 'NOT', 'AND', 'OR', 
          'LPAREN', 'RPAREN', 'ASSIGN', 'CHARCHAR', 'NUMBER') + tuple(kwords.values())

# States for different types of blocks of code
# states = (
#     ('IF_BLOCK', 'exclusive'),
#     ('WHILE_BLOCK', 'exclusive')
# )

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_EOF = r'EOF'
t_INCR = r'\+\+'
t_DECR = r'--'
t_ADDEQ = r'\+='
t_SUBEQ = r'\-='
t_MULTEQ = r'\*='
t_DIVEQ = r'/='
t_ADD = r'\+'
t_SUB = r'-'  
t_MULT = r'\*'
t_DIV = r'/'
t_GREQUAL = r'>='
t_LEQUAL = r'<='
t_ISNOT = r'~='
t_GREATER = r'>'
t_LESS = r'<'
t_EQUALS = r'=' # ??
t_NOT = r'~'
t_AND = r'&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\<-'

# HEY CHAR Rule for variable chars
def t_CHARCHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = kwords.get(t.value, 'CHARCHAR') # Checks for key words, otherwise Char Char
    return t

# Number Rule
def t_NUMBER(t):
    # r'\d+(\.\d+)?' # 1 or more digits/floats
    # if '.' not in t.value:
    #     t.value = int(t.value)
    # else:
    #     t.value = float(t.value)
    # return t
    r'\d+'
    t.value = int(t.value)
    return t

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

# --- Parser
#   expression : term ADD term
#              | term SUB term
#              | term
#
#   term       : factor MULT factor
#              | factor DIV factor
#              | factor
#
#   factor     : NUMBER
#              | CHARCHAR
#              | ADD factor
#              | SUB factor
#              | LPAREN expression RPAREN

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UNARY')
)

chars = {}

def p_statement_assign(p):
    'statement : CHARCHAR ASSIGN expression'
    chars[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MULT expression
                  | expression DIV expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_unary(p):
    "expression : SUB expression %prec UNARY" # %prec - Precedence token
    p[0] = -p[2]

def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_char(p):
    "expression : CHARCHAR"
    try:
        p[0] = chars[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# # Iterates through file, tokenizing each item
# file = sys.stdin.readlines()
# for i in range(len(file)):
#     lexer.input(file[i])
#     for token in lexer:
#         print(token) # (Token Type, Value, Line Number, Position)

# # Manually create EOF Token
# eof_token = LexToken()
# eof_token.type = t_EOF
# eof_token.value = None
# eof_token.lineno = lexer.lineno
# eof_token.lexpos = lexer.lexpos
# print(eof_token)
    
parser = yacc.yacc()
# while True:
#     ast = parser.parse(input("epxr < "))
#     print(ast)
while True:
    try:
        s = input('expr > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)