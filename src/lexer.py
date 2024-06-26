from ply.lex import lex
from ply.yacc import yacc
from collections import deque
from operator import add, sub, mul, truediv

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
    # 'create' : 'CREATE',
    'tartarus' : 'TARTARUS',
    # 'die' : 'DIE',
    # 'retaliate' : 'RETALIATE',
    # 'gate' : 'GATE'
}

# Token Types
tokens = ('EOF', 'INCR', 'DECR', 'ADD', 'SUB', 'MULT', 'DIV', 
          'GREQUAL', 'LEQUAL', 'ISNOT', 'ASSIGN', 'GREATER', 'LESS', 'EQUALS', 
          'NOT', 'AND', 'OR', 'LPAREN', 'RPAREN',
          'CHARCHAR', 'SCRIPT', 'NUMBER') + tuple(kwords.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
# t_EOF = r'EOF'
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
    r'\-?\d+(\.\d+)?' # 1 or more digits/floats
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

# Precedence for operations
precedence = (
    ('nonassoc', 'LESS', 'GREATER', 'LEQUAL', 'GREQUAL'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UNARY')
)

characters = {}

def p_statement_if(p): # 7 10 9
    '''
    expression : IF LPAREN expression RPAREN ACTION expression CUT opt_el
              | IF LPAREN expression RPAREN ACTION expression CUT elif_statements opt_el
    '''
    if len(p) == 9: # If it's just an if
        p[0] = ('if', p[3], p[6], None, p[8])
    else: 
        p[0] = ('if', p[3], p[6], p[8], p[9])

def p_elif_statements(p):
    '''
    elif_statements : elif_statement
                    | elif_statements elif_statement
    '''
    if len(p) == 2: 
        p[0] = [p[1]]
    else:  # Multiple elif statements
        p[0] = p[1] + [p[2]]

def p_elif_statement(p):
    '''
    elif_statement : ELIF LPAREN expression RPAREN ACTION expression CUT
    '''
    p[0] = ('elif', p[3], p[6])

def p_opt_el(p):
    '''
    opt_el : EL ACTION expression CUT
           |
    '''
    if len(p) == 5:
        p[0] = ('el', p[3])
    else:
        p[0] = None

def p_statement_while(p):
    '''
    expression : SCENE LPAREN expression RPAREN ACTION expression CUT
    '''
    p[0] = ('scene', p[3], p[6])

def p_statement_for(p):
    '''
    expression : FROM LPAREN expression RPAREN TO LPAREN expression RPAREN ACTION expression CUT 
    '''
    p[0] = ('from_to', p[3], p[7], p[10])
    
def p_statement_deal(p):
    '''
    expression : DEAL LPAREN expression RPAREN ACTION ex_list CUT
    '''
    p[0] = ('deal', p[3], p[6])

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
    ex : EX expression ACTION expression CUT
    '''
    p[0] = ('ex', p[2], p[4])

# def p_statement_expr(p):
#     '''
#     statement : expression
#     '''
#     p[0] = p[1]

def p_expression_binop(p):
    '''
    expression : expression ADD expression
               | expression SUB expression
               | expression MULT expression
               | expression DIV expression
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_comparison(p):
    '''
    expression : expression LESS expression
               | expression GREATER expression
               | expression LEQUAL expression
               | expression GREQUAL expression
               | expression EQUALS expression
               | expression ISNOT expression
    '''
    p[0] = ('comparison', p[2], p[1], p[3])

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
        
def p_expression_tartarus(p):
    '''
    expression : TARTARUS
    '''
    p[0] = ('tartarus', None)

def p_statement_script(p): # Hold please *Waiting music*
    '''
    expression : SCRIPT
    '''
    p[0] = ('script', p[1]) # SCRIPT

def p_expression_assign(p):
    '''
    expression : CHARCHAR ASSIGN expression
               | CHARCHAR INCR
               | CHARCHAR DECR
    '''
    if len(p) == 4:
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = ('assign', p[1], p[2])

def p_expression(p):
    '''
    expression : NUMBER
               | negative_number
               | CHARCHAR
               | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        if isinstance(p[1], float):
            p[0] = ('number', p[1])
        else:
            p[0] = ('CHARCHAR', p[1])
    elif p[1] == '(':
        p[0] = ['grouped', p[2]]

def p_negative_number(p):
    '''
    negative_number : SUB NUMBER %prec UNARY
    '''
    p[0] = ('number', -p[2])

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")
        
# Build the parser
parser = yacc()

# Evaluation function
def evaluate_expression(expression):
    if isinstance(expression, tuple):
        # Evaluate If statements
        if expression[0] == 'if':
            condition = evaluate_expression(expression[1])
            if condition == "Truth":
                return evaluate_expression(expression[2])
            elif expression[4] is not None and expression[3] is None: # el statement, No elif statements
                return evaluate_expression(expression[4][1])
            elif expression[3] is not None: # 1 or more elif statements
                for case in expression[3]:
                    condition = evaluate_expression(case[1])
                    if condition == "Truth":
                        return evaluate_expression(case[2])
                if expression[4] is not None: # Evaluate el statement if all elif statements are false
                    return evaluate_expression(expression[4][1])
            else:
                return None # Nothing could be done, RIP
            
        # Evaluate Switch cases
        elif expression[0] == 'deal':
            condition = evaluate_expression(expression[1])
            cases = expression[2]
            result = None
            for case in cases:
                case_condition = evaluate_expression(case[1])
                if case_condition == condition:
                    result = evaluate_expression(case[2])
                    break
            if result is None and len(expression) > 3:
                result = evaluate_expression(expression[3])
            return result
        
        # Evaluate Scene loop
        elif expression[0] == 'scene': 
            condition = expression[1]
            action = expression[2]
            result = None
            while evaluate_expression(condition) == "Truth":
                result = evaluate_expression(action)
            return result

        # Evaluate From_to loop
        elif expression[0] == 'from_to':
            start_cond = evaluate_expression(expression[1])
            end_cond = evaluate_expression(expression[2])
            action = expression[3]
            result = None
            for i in range(int(start_cond), int(end_cond)+1):
                result = evaluate_expression(action)
            return result

        # Evaluate Basic operations
        elif expression[0] == 'number':
            return expression[1]
        elif expression[0] == 'script':
            return expression[1]
        elif expression[0] == 'CHARCHAR':
            var_name = expression[1]
            if var_name in characters:
                return characters[var_name]
            else:
                print(f"Error: Variable '{var_name}' is undefined")
                return None
            
        # Evaluate Binary operations
        elif expression[0] == 'binop':
            op = expression[1]
            left = evaluate_expression(expression[2])
            right = evaluate_expression(expression[3])
            if op == '+':
                return add(left, right)
            elif op == '-':
                return sub(left, right)
            elif op == '*':
                return mul(left, right)
            elif op == '/':
                return truediv(left, right)
            
        # Evaluate Comparisons
        elif expression[0] == 'comparison':
            op = expression[1]
            left = evaluate_expression(expression[2])
            right = evaluate_expression(expression[3])
            res = None
            if op == '<':
                res = left < right
            elif op == '>':
                res = left > right
            elif op == '<=':
                res = left <= right
            elif op == '>=':
                res = left >= right
            elif op == '=?':
                res = left == right
            elif op == '~=': # IsNot
                res = left != right
            if res == True:
                return "Truth"
            else:
                return "Lie"
            
        # Evaluate Logic expressions
        elif expression[0] == 'logic':
            if len(expression) == 4:
                op = expression[1]
                left = evaluate_expression(expression[2])
                right = evaluate_expression(expression[3])
                if op == 'AND':
                    if left == "Truth" and right == "Truth":
                        return "Truth"
                    else:
                        return "Lie"
                elif op == 'OR':
                    if left == "Truth" or right == "Truth":
                        return "Truth"
                    else:
                        return "Lie"
            elif len(expression) == 3:
                op = expression[1]
                left = evaluate_expression(expression[2])
                if op == 'NOT':
                    if left == "Truth":
                        return "Lie"
                    else:
                        return "Truth"
                
        # Evaluate Assignments
        elif expression[0] == 'assign':
            var_name = expression[1]
            expr_ast = expression[2]
            if expr_ast == '++':
                characters[var_name] += 1
                return characters[var_name]
            elif expr_ast == '--':
                characters[var_name] -= 1
                return characters[var_name]
            else:
                result = evaluate_expression(expr_ast)
                if (result is not None or (expr_ast[0] == 'tartarus')): # Only update if exists
                    characters[var_name] = result
                return result
            
        # Evaluate null
        elif expression[0] == 'tartarus':
            return None
        
    elif isinstance(expression, str):
        return expression
    
    # Evaluate Grouped Expressions
    elif isinstance(expression, list) and expression[0] == 'grouped':
        return evaluate_expression(expression[1])
    else:
        return expression

file_name = input("Enter the file name: ")
try:
    # Open sesame
    with open(file_name, 'r') as file:
        lines = file.readlines() # Literacy

        # Iterate over each line
        for line in lines:
            if not line.strip(): # Skip empty lines
                continue
            
            try: # Parse and evaluate
                ast = parser.parse(line, lexer=lexer)
                result = evaluate_expression(ast)
                print(f"{line.strip()} \nResult: {result}") # Make it look nice
            except Exception as e:
                print(f"Syntax error: {e}") # Erroar
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")

