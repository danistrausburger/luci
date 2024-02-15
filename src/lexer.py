from ply.lex import lex
# --- Tokenizer

# All tokens must be named in advance.
tokens = ('ADD', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN',
          'CHAR', 'NUMBER')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_ADD = r'\+'
t_MINUS = r'-'  
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_CHAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Our work shall continue to grow **Maniacal Laughter**

def t_CHAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #t.type = 'CHAR' # Set token type
    return t
# Number token rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    #t.type = 'NUMBER' # Set token type
    return t
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()
lexer.input('2 + 3 * 2')

for token in lexer:
    print(token)