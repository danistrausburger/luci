from ply.lex import lex
import sys

# --- Tokenizer
kwords = {
    'if' : 'IF',
    'elif' : 'ELIF',
    'el' : 'EL',
    'scene' : 'SCENE',
    'every' : 'EVERY',
    'handle' : 'HANDLE',
    'ex' : 'EX',
    'action' : 'ACTION',
    'cut' : 'CUT'
}

# Token Types
tokens = ('EOF', 'ADD', 'SUB', 'MULT', 'DIV', 'GREQUAL', 'LEQUAL',
          'ISNOT', 'GREATER', 'LESS', 'EQUALS', 'NOT', 'AND', 'OR', 
          'LPAREN', 'RPAREN', 'ASSIGNED', 'CHARCHAR', 'NUMBER') + tuple(kwords.values())

# States for different types of blocks of code
# states = (
#     ('IF_BLOCK', 'exclusive'),
#     ('WHILE_BLOCK', 'exclusive')
# )

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_EOF = r'EOF'
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
t_ASSIGNED = r'\<-'

# HEY CHAR Rule for variable names
def t_CHARCHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = kwords.get(t.value, 'CHARCHAR') # Checks for key words, otherwise Char Char
    return t

# Number Rule
def t_NUMBER(t):
    r'\d+' # 1 or more digits
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

# Iterates through file, tokenizing each item
file = sys.stdin.readlines()
for i in range(len(file)):
    lexer.input(file[i])
    for token in lexer:
        print(token) # (Token Type, Value, Line Number, Position)