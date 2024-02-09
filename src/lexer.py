# --- Tokenizer

# All tokens must be named in advance.
tokens = ('ADD', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN',
          'CHARACTER', 'NUMBER')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_ADD = r'\+'
t_MINUS = r'-'  
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CHARACTER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Our work shall continue to grow **Maniacal Laughter**