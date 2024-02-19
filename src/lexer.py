from ply.lex import lex
import sys

# --- Tokenizer
kwords = { # Need to add looping terms
    'if' : 'IF',
    'elif' : 'ELIF',
    'el' : 'EL',
    'while' : 'WHILE',
    'every' : 'EVERY',
    'handle' : 'HANDLE',
    'ex' : 'EX'
} # ~Kooks~ What a key word

# Token Types
tokens = ('EOF', 'ADD', 'MINUS', 'MULT', 'DIV', 'GREQUAL', 'LEQUAL',
          'ISNOT', 'GREATER', 'LESS', 'EQUALS', 'NOT', 'AND', 'OR', 
          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ASSIGNED',
          'CHARCHAR', 'NUMBER') + tuple(kwords.values())

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
t_MINUS = r'-'  
t_MULT = r'\*'
t_DIV = r'/'
t_GREQUAL = r'>=' # We are qrequals
t_LEQUAL = r'<=' # That's illequal
t_ISNOT = r'~=' # That is not where this ends *radio static*
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
t_ASSIGNED = r'\<-'

# Our work shall continue to grow **Maniacal Laughter**
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
lexer = lex() # LUTHOR

# lexer.input('2 + 3 * 2')
# lexer.input('abc Hello_World Zzz')
# lexer.input('x <- 5')
# lexer.input('if (x =? 1) {x <- 5} \n x <- x + 5')
# lexer.input('x =? y')

# Reading command line arguments
# text = input('Enter your expression >')
# lexer.input(text)

# Iterates through file, tokenizing each item
file = sys.stdin.readlines()
for i in range(len(file)):
    lexer.input(file[i])
    for token in lexer:
        print(token) # (Token Type, Value, Line Number, Position)

# Must also be able to take in a file (EOF)
# Take in stdin?