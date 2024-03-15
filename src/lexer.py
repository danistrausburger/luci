from ply.lex import lex, LexToken
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
# FROM __ TO __ (FOR LOOP)
# Token Types
tokens = ('EOF', 'INCR', 'DECR', 'ADDEQ', 'SUBEQ', 'MULTEQ', 'DIVEQ', 'ADD', 'SUB', 'MULT', 'DIV', 'GREQUAL', 'LEQUAL',
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
t_INCR = r'\++'
t_DECR = r'\--'
t_ADDDEQ = r'\+='
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
t_EQUALS = r'=\?'
t_NOT = r'~'
t_AND = r'&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\<-'

# HEY CHAR Rule for variable names
def t_CHARCHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = kwords.get(t.value, 'CHARCHAR') # Checks for key words, otherwise Char Char
    return t

# Number Rule
def t_NUMBER(t):
    r'\d+(\.\d+)?' # 1 or more digits/floats
    if '.' not in t.value:
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

# Iterates through file, tokenizing each item
file = sys.stdin.readlines()
for i in range(len(file)):
    lexer.input(file[i])
    for token in lexer:
        print(token) # (Token Type, Value, Line Number, Position)

# Manually create EOF Token
eof_token = LexToken()
eof_token.type = t_EOF
eof_token.value = None
eof_token.lineno = lexer.lineno
eof_token.lexpos = lexer.lexpos # Let's gooooo dude I'm the best
print(eof_token)