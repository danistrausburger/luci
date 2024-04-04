
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION ADD AND ASSIGN CHARCHAR CREATE CUT DEAL DECR DIE DIV EL ELIF EOF EQUALS EX FROM GATE GREATER GREQUAL IF INCR ISNOT LBRACE LEQUAL LESS LIE LPAREN MULT NOT NUMBER OR RBRACE RETALIATE RPAREN SCENE SCRIPT SUB TARTARUS TO TRUTH\n    statement : IF LPAREN expression RPAREN ACTION statement CUT\n              | IF LPAREN expression RPAREN ACTION statement CUT elif_statements opt_el\n              | IF LPAREN expression RPAREN ACTION statement CUT opt_el\n    \n    elif_statements : elif_statement\n                    | elif_statements elif_statement\n    \n    elif_statement : ELIF LPAREN expression RPAREN ACTION expression CUT\n    \n    opt_el : EL ACTION statement CUT\n           |\n    \n    statement : SCENE LPAREN expression RPAREN ACTION statement CUT\n    \n    statement : FROM LPAREN expression RPAREN TO LPAREN expression RPAREN ACTION statement CUT \n    \n    statement : DEAL LPAREN expression RPAREN ACTION ex_list CUT\n    \n    ex_list : ex_list ex \n        | ex\n    \n    ex : EX expression ACTION statement CUT\n    \n    statement : expression\n    \n    expression : expression ADD expression\n               | expression SUB expression\n               | expression MULT expression\n               | expression DIV expression\n               | expression INCR\n               | expression DECR\n    \n    expression : expression LESS expression\n               | expression GREATER expression\n               | expression LEQUAL expression\n               | expression GREQUAL expression\n               | expression EQUALS expression\n               | expression ISNOT expression\n    \n    expression : expression AND expression\n               | expression OR expression\n               | NOT expression\n    \n    statement : SCRIPT\n    \n    expression : CHARCHAR ASSIGN expression\n               | CHARCHAR ASSIGN statement\n    \n    expression : term\n               | expression ADD term\n               | expression SUB term\n               | expression MULT term\n               | expression DIV term\n    \n    term : factor\n         | term MULT factor\n         | term DIV factor\n    \n    factor : NUMBER\n           | CHARCHAR\n           | LPAREN expression RPAREN\n           | ADD factor\n           | SUB factor\n    '
    
_lr_action_items = {'IF':([0,39,71,72,93,96,98,],[2,2,2,2,2,2,2,]),'SCENE':([0,39,71,72,93,96,98,],[5,5,5,5,5,5,5,]),'FROM':([0,39,71,72,93,96,98,],[6,6,6,6,6,6,6,]),'DEAL':([0,39,71,72,93,96,98,],[7,7,7,7,7,7,7,]),'SCRIPT':([0,39,71,72,93,96,98,],[8,8,8,8,8,8,8,]),'NOT':([0,3,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,71,72,77,80,93,96,97,98,107,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'CHARCHAR':([0,3,9,10,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,40,41,71,72,77,80,93,96,97,98,107,],[12,12,36,36,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,36,36,12,12,12,12,12,12,12,12,12,]),'NUMBER':([0,3,9,10,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,40,41,71,72,77,80,93,96,97,98,107,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'LPAREN':([0,2,3,5,6,7,9,10,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,40,41,71,72,73,77,80,91,93,96,97,98,107,],[3,16,3,32,33,34,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,77,3,3,97,3,3,3,3,3,]),'ADD':([0,3,4,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,72,77,80,81,82,83,84,86,87,88,89,93,94,95,96,97,98,101,104,106,107,108,109,],[9,9,18,-31,9,9,9,-43,-34,-39,-42,9,18,9,9,9,9,-20,-21,9,9,9,9,9,9,9,9,9,9,9,-45,-43,-46,18,9,9,9,18,-44,18,-34,18,-34,18,-34,18,-34,18,18,18,18,18,18,18,18,18,18,18,18,-33,-40,-41,9,9,9,9,-1,-9,18,-11,18,-8,-3,-4,9,-2,-5,9,9,9,18,-7,-10,9,18,-6,]),'SUB':([0,3,4,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,71,72,77,80,81,82,83,84,86,87,88,89,93,94,95,96,97,98,101,104,106,107,108,109,],[10,10,19,-31,10,10,10,-43,-34,-39,-42,10,19,10,10,10,10,-20,-21,10,10,10,10,10,10,10,10,10,10,10,-45,-43,-46,19,10,10,10,19,-44,19,-34,19,-34,19,-34,19,-34,19,19,19,19,19,19,19,19,19,19,19,19,-33,-40,-41,10,10,10,10,-1,-9,19,-11,19,-8,-3,-4,10,-2,-5,10,10,10,19,-7,-10,10,19,-6,]),'$end':([1,4,8,12,13,14,15,22,23,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,65,66,81,82,84,87,88,89,94,95,104,106,109,],[0,-15,-31,-43,-34,-39,-42,-20,-21,-45,-43,-46,-30,-44,-16,-34,-17,-34,-18,-34,-19,-34,-22,-23,-24,-25,-26,-27,-28,-29,-15,-33,-40,-41,-1,-9,-11,-8,-3,-4,-2,-5,-7,-10,-6,]),'CUT':([4,8,12,13,14,15,22,23,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,65,66,75,76,78,79,81,82,84,85,87,88,89,94,95,99,100,102,103,104,106,108,109,],[-15,-31,-43,-34,-39,-42,-20,-21,-45,-43,-46,-30,-44,-16,-34,-17,-34,-18,-34,-19,-34,-22,-23,-24,-25,-26,-27,-28,-29,-15,-33,-40,-41,81,82,84,-13,-1,-9,-11,-12,-8,-3,-4,-2,-5,103,104,106,-14,-7,-10,109,-6,]),'MULT':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[20,-31,-43,40,-39,-42,20,-20,-21,-45,-43,-46,20,20,-44,20,40,20,40,20,40,20,40,20,20,20,20,20,20,20,20,20,20,20,20,-33,-40,-41,-1,-9,20,-11,20,-8,-3,-4,-2,-5,20,-7,-10,20,-6,]),'DIV':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[21,-31,-43,41,-39,-42,21,-20,-21,-45,-43,-46,21,21,-44,21,41,21,41,21,41,21,41,21,21,21,21,21,21,21,21,21,21,21,21,-33,-40,-41,-1,-9,21,-11,21,-8,-3,-4,-2,-5,21,-7,-10,21,-6,]),'INCR':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[22,-31,-43,-34,-39,-42,22,-20,-21,-45,-43,-46,22,22,-44,22,-34,22,-34,22,-34,22,-34,22,22,22,22,22,22,22,22,22,22,22,22,-33,-40,-41,-1,-9,22,-11,22,-8,-3,-4,-2,-5,22,-7,-10,22,-6,]),'DECR':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[23,-31,-43,-34,-39,-42,23,-20,-21,-45,-43,-46,23,23,-44,23,-34,23,-34,23,-34,23,-34,23,23,23,23,23,23,23,23,23,23,23,23,-33,-40,-41,-1,-9,23,-11,23,-8,-3,-4,-2,-5,23,-7,-10,23,-6,]),'LESS':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[24,-31,-43,-34,-39,-42,24,-20,-21,-45,-43,-46,24,24,-44,24,-34,24,-34,24,-34,24,-34,24,24,24,24,24,24,24,24,24,24,24,24,-33,-40,-41,-1,-9,24,-11,24,-8,-3,-4,-2,-5,24,-7,-10,24,-6,]),'GREATER':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[25,-31,-43,-34,-39,-42,25,-20,-21,-45,-43,-46,25,25,-44,25,-34,25,-34,25,-34,25,-34,25,25,25,25,25,25,25,25,25,25,25,25,-33,-40,-41,-1,-9,25,-11,25,-8,-3,-4,-2,-5,25,-7,-10,25,-6,]),'LEQUAL':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[26,-31,-43,-34,-39,-42,26,-20,-21,-45,-43,-46,26,26,-44,26,-34,26,-34,26,-34,26,-34,26,26,26,26,26,26,26,26,26,26,26,26,-33,-40,-41,-1,-9,26,-11,26,-8,-3,-4,-2,-5,26,-7,-10,26,-6,]),'GREQUAL':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[27,-31,-43,-34,-39,-42,27,-20,-21,-45,-43,-46,27,27,-44,27,-34,27,-34,27,-34,27,-34,27,27,27,27,27,27,27,27,27,27,27,27,-33,-40,-41,-1,-9,27,-11,27,-8,-3,-4,-2,-5,27,-7,-10,27,-6,]),'EQUALS':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[28,-31,-43,-34,-39,-42,28,-20,-21,-45,-43,-46,28,28,-44,28,-34,28,-34,28,-34,28,-34,28,28,28,28,28,28,28,28,28,28,28,28,-33,-40,-41,-1,-9,28,-11,28,-8,-3,-4,-2,-5,28,-7,-10,28,-6,]),'ISNOT':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[29,-31,-43,-34,-39,-42,29,-20,-21,-45,-43,-46,29,29,-44,29,-34,29,-34,29,-34,29,-34,29,29,29,29,29,29,29,29,29,29,29,29,-33,-40,-41,-1,-9,29,-11,29,-8,-3,-4,-2,-5,29,-7,-10,29,-6,]),'AND':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[30,-31,-43,-34,-39,-42,30,-20,-21,-45,-43,-46,30,30,-44,30,-34,30,-34,30,-34,30,-34,30,30,30,30,30,30,30,30,30,30,30,30,-33,-40,-41,-1,-9,30,-11,30,-8,-3,-4,-2,-5,30,-7,-10,30,-6,]),'OR':([4,8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,86,87,88,89,94,95,101,104,106,108,109,],[31,-31,-43,-34,-39,-42,31,-20,-21,-45,-43,-46,31,31,-44,31,-34,31,-34,31,-34,31,-34,31,31,31,31,31,31,31,31,31,31,31,31,-33,-40,-41,-1,-9,31,-11,31,-8,-3,-4,-2,-5,31,-7,-10,31,-6,]),'RPAREN':([8,12,13,14,15,17,22,23,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,81,82,83,84,87,88,89,94,95,101,104,106,109,],[-31,-43,-34,-39,-42,43,-20,-21,-45,-43,-46,-30,67,-44,-16,-34,-17,-34,-18,-34,-19,-34,-22,-23,-24,-25,-26,-27,-28,-29,68,69,70,-15,-33,-40,-41,-1,-9,92,-11,-8,-3,-4,-2,-5,105,-7,-10,-6,]),'ACTION':([8,12,13,14,15,22,23,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,65,66,67,68,70,81,82,84,86,87,88,89,90,92,94,95,104,105,106,109,],[-31,-43,-34,-39,-42,-20,-21,-45,-43,-46,-30,-44,-16,-34,-17,-34,-18,-34,-19,-34,-22,-23,-24,-25,-26,-27,-28,-29,-15,-33,-40,-41,71,72,74,-1,-9,-11,93,-8,-3,-4,96,98,-2,-5,-7,107,-10,-6,]),'ASSIGN':([12,],[39,]),'TO':([69,],[73,]),'EX':([74,78,79,85,103,],[80,80,-13,-12,-14,]),'EL':([81,87,89,95,109,],[90,90,-4,-5,-6,]),'ELIF':([81,87,89,95,109,],[91,91,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,39,71,72,93,96,98,],[1,64,75,76,99,100,102,]),'expression':([0,3,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,71,72,77,80,93,96,97,98,107,],[4,17,38,42,44,46,48,50,52,53,54,55,56,57,58,59,60,61,62,63,4,4,83,86,4,4,101,4,108,]),'term':([0,3,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,71,72,77,80,93,96,97,98,107,],[13,13,13,13,45,47,49,51,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'factor':([0,3,9,10,11,16,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,39,40,41,71,72,77,80,93,96,97,98,107,],[14,14,35,37,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,65,66,14,14,14,14,14,14,14,14,14,]),'ex_list':([74,],[78,]),'ex':([74,78,],[79,85,]),'elif_statements':([81,],[87,]),'opt_el':([81,87,],[88,94,]),'elif_statement':([81,87,],[89,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IF LPAREN expression RPAREN ACTION statement CUT','statement',7,'p_statement_if','lexer.py',94),
  ('statement -> IF LPAREN expression RPAREN ACTION statement CUT elif_statements opt_el','statement',9,'p_statement_if','lexer.py',95),
  ('statement -> IF LPAREN expression RPAREN ACTION statement CUT opt_el','statement',8,'p_statement_if','lexer.py',96),
  ('elif_statements -> elif_statement','elif_statements',1,'p_elif_statements','lexer.py',107),
  ('elif_statements -> elif_statements elif_statement','elif_statements',2,'p_elif_statements','lexer.py',108),
  ('elif_statement -> ELIF LPAREN expression RPAREN ACTION expression CUT','elif_statement',7,'p_elif_statement','lexer.py',119),
  ('opt_el -> EL ACTION statement CUT','opt_el',4,'p_opt_el','lexer.py',125),
  ('opt_el -> <empty>','opt_el',0,'p_opt_el','lexer.py',126),
  ('statement -> SCENE LPAREN expression RPAREN ACTION statement CUT','statement',7,'p_statement_while','lexer.py',135),
  ('statement -> FROM LPAREN expression RPAREN TO LPAREN expression RPAREN ACTION statement CUT','statement',11,'p_statement_for','lexer.py',141),
  ('statement -> DEAL LPAREN expression RPAREN ACTION ex_list CUT','statement',7,'p_statement_deal','lexer.py',147),
  ('ex_list -> ex_list ex','ex_list',2,'p_ex_list','lexer.py',154),
  ('ex_list -> ex','ex_list',1,'p_ex_list','lexer.py',155),
  ('ex -> EX expression ACTION statement CUT','ex',5,'p_ex','lexer.py',164),
  ('statement -> expression','statement',1,'p_statement_expr','lexer.py',170),
  ('expression -> expression ADD expression','expression',3,'p_expression_binop','lexer.py',176),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','lexer.py',177),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','lexer.py',178),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','lexer.py',179),
  ('expression -> expression INCR','expression',2,'p_expression_binop','lexer.py',180),
  ('expression -> expression DECR','expression',2,'p_expression_binop','lexer.py',181),
  ('expression -> expression LESS expression','expression',3,'p_expression_comparison','lexer.py',198),
  ('expression -> expression GREATER expression','expression',3,'p_expression_comparison','lexer.py',199),
  ('expression -> expression LEQUAL expression','expression',3,'p_expression_comparison','lexer.py',200),
  ('expression -> expression GREQUAL expression','expression',3,'p_expression_comparison','lexer.py',201),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_comparison','lexer.py',202),
  ('expression -> expression ISNOT expression','expression',3,'p_expression_comparison','lexer.py',203),
  ('expression -> expression AND expression','expression',3,'p_expression_logic','lexer.py',220),
  ('expression -> expression OR expression','expression',3,'p_expression_logic','lexer.py',221),
  ('expression -> NOT expression','expression',2,'p_expression_logic','lexer.py',222),
  ('statement -> SCRIPT','statement',1,'p_statement_script','lexer.py',234),
  ('expression -> CHARCHAR ASSIGN expression','expression',3,'p_expression_assign','lexer.py',240),
  ('expression -> CHARCHAR ASSIGN statement','expression',3,'p_expression_assign','lexer.py',241),
  ('expression -> term','expression',1,'p_expression','lexer.py',247),
  ('expression -> expression ADD term','expression',3,'p_expression','lexer.py',248),
  ('expression -> expression SUB term','expression',3,'p_expression','lexer.py',249),
  ('expression -> expression MULT term','expression',3,'p_expression','lexer.py',250),
  ('expression -> expression DIV term','expression',3,'p_expression','lexer.py',251),
  ('term -> factor','term',1,'p_term','lexer.py',267),
  ('term -> term MULT factor','term',3,'p_term','lexer.py',268),
  ('term -> term DIV factor','term',3,'p_term','lexer.py',269),
  ('factor -> NUMBER','factor',1,'p_factor','lexer.py',280),
  ('factor -> CHARCHAR','factor',1,'p_factor','lexer.py',281),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','lexer.py',282),
  ('factor -> ADD factor','factor',2,'p_factor','lexer.py',283),
  ('factor -> SUB factor','factor',2,'p_factor','lexer.py',284),
]
