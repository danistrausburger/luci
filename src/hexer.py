from ply.lex import lex
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
tokens = ('EOF', 'INCR', 'DECR', 'ADD', 'SUB', 'MULT', 'DIV', 
          'GREQUAL', 'LEQUAL', 'ISNOT', 'ASSIGN', 'GREATER', 'LESS', 'EQUALS', 
          'NOT', 'AND', 'OR', 'LPAREN', 'RPAREN',
          'CHARCHAR', 'SCRIPT', 'NUMBER') + tuple(kwords.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_EOF = r'EOF'
t_INCR = r'\+\+'
t_DECR = r'\-\-'
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
t_AND = r'\&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Script rules for strings
def t_SCRIPT(t):
    r'\"([^\\"]|\\")*\"'
    t.value = t.value[1:-1]  # Remove double quotes from the value
    return t

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

precedence = (
    ('nonassoc', 'LESS', 'GREATER', 'LEQUAL', 'GREQUAL'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UNARY')
)

characters = {}

def p_statement_if(p):
    '''
    statement : IF LPAREN expression RPAREN ACTION statement CUT
              | IF LPAREN expression RPAREN ACTION statement CUT elif_statements opt_el
              | IF LPAREN expression RPAREN ACTION statement CUT opt_el
    '''
    if len(p) == 8: # If it's just an if
        p[0] = ('if', p[3], p[6])
    elif len(p) == 9: # If else
        p[0] = ('if_el', p[3], p[6], p[8])
    else: 
        p[0] = ('if_elif_el', p[3], p[6], p[8], p[9])

def p_elif_statements(p): # Won't print out elif statements after the first
    '''
    elif_statements : elif_statement
                    | elif_statements elif_statement
    '''
    if len(p) == 2: 
        p[0] = [p[1]]
    # elif len(p) == 3:
    #     p[0] = []
    else:  # Multiple elif statements
        p[0] = p[1] + [p[2]]

def p_elif_statement(p):
    '''
    elif_statement : ELIF LPAREN expression RPAREN ACTION expression CUT
    '''
    p[0] = ('elif', p[3], p[6])

def p_opt_el(p):
    '''
    opt_el : EL ACTION statement CUT
           |
    '''
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_statement_while(p):
    '''
    statement : SCENE LPAREN expression RPAREN ACTION statement CUT
    '''
    p[0] = ('scene', p[3], p[6])

def p_statement_for(p):
    '''
    statement : FROM LPAREN expression RPAREN TO LPAREN expression RPAREN ACTION statement CUT 
    '''
    p[0] = ('from_to', p[3], p[7], p[10])
    
def p_statement_deal(p):
    '''
    statement : DEAL LPAREN expression RPAREN ACTION ex_list CUT
    '''
    p[0] = ('deal', p[3], p[6])
    print(p[0])

def p_ex_list(p):
    '''
    ex_list : ex_list ex 
        | ex
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_ex(p):
    '''
    ex : EX expression ACTION statement CUT
    '''
    p[0] = ('ex', p[2], p[4])

def p_statement_assign(p):
    '''statement : CHARCHAR ASSIGN expression
                 | CHARCHAR INCR
                 | CHARCHAR DECR'''
    if p[2] == '<-':
        characters[p[1]] = p[3]
    elif p[2] == '++':
        characters[p[1]] = characters[p[1]] + 1
    elif p[2] == '--':
        characters[p[1]] = characters[p[1]] - 1

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]
    print(p[0]) # Dialogue print token

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
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Erroar: Cannot divide by 0 idiot")
        else:
            p[0] = p[1] / p[3]
    elif p[2] == '++':
        p[0] = p[1] + 1
    elif p[2] == '--':
        p[0] = p[1] - 1

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

def p_expression_logic(p):
    '''
    expression : expression AND expression
               | expression OR expression
               | NOT expression
    '''
    if len(p) == 4:
        if p[2] == '&':
            p[0] = ('logic', 'AND', p[1], p[3])
        elif p[2] == '|':
            p[0] = ('logic', 'OR', p[1], p[3])
    elif len(p) == 3:
        p[0] = ('logic', 'NOT', p[2])

def p_expression_unary(p):
    '''expression : SUB expression %prec UNARY''' # %prec - Precedence token
    p[0] = -p[2]

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_char(p):
    '''expression : CHARCHAR'''
    try:
        p[0] = characters[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_expression_script(p):
    '''
    expression : SCRIPT
    '''
    p[0] = p[1] # SCRIPT

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")
        
# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('expr > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
