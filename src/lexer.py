from ply.lex import lex

# --- Tokenizer
kwords = { # Need to add looping terms
    'if' : 'IF',
    'elif' : 'ELIF',
    'el' : 'EL'
} # ~Kooks~ What a key word

# Token Types
tokens = ('ADD', 'MINUS', 'MULT', 'DIV', 'GREQUAL', 'LEQUAL',
          'ISNOT', 'GREATER', 'LESS', 'EQUALS', 'AND', 'OR', 
          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ASSIGNED',
          'CHAR', 'NUMBER') + tuple(kwords.values())

# States for different types of blocks of code
# states = (
#     ('IF_BLOCK', 'exclusive'),
#     ('WHILE_BLOCK', 'exclusive')
# )

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
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
t_AND = r'&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGNED = r'\<-'

# Our work shall continue to grow **Maniacal Laughter**
# HEY CHAR Rule for variable names
def t_CHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = kwords.get(t.value, 'CHAR') # Checks for key words, otherwise Char Char
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
lexer.input('if (x =? 1) {x <- 5} \n x <- x + 5')
# lexer.input('x =? y')

for token in lexer:
    print(token) # (Token Type, Value, Line Number, Position)

# Must also be able to take in a file (EOF)
# Take in stdin?