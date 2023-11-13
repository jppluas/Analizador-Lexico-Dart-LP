import ply.yacc as sint
from lexico import tokens

def p_statement(p):
 '''
 statement : assignment
           | print
 '''

def p_expresion(p):
    '''  expresion : value
        |   expresion op expresion
        |   expresion op value
        |   value op value
        |   LPAREN expresion op expresion RPAREN
        |   LPAREN expresion op value RPAREN
        |   LPAREN value op value RPAREN
    '''

def p_op(p):
    ''' op : PLUS
        |   MINUS
        |   TIMES
        |   DIVIDE
    '''

def p_assignment(p):
    '''  assignment : modifier type nullable IDENTIFIER ASSIGN expresion SEMICOLON
    '''

def p_print(p):
    '''  print : PRINT LPAREN expresion RPAREN SEMICOLON
    '''

def p_list(p):
    ''' list : LSQUARE RSQUARE
            | LSQUARE values RSQUARE
    
    '''

def p_type(p):
    ''' type : INTEGER_TYPE
                | DOUBLE_TYPE
                | BOOLEAN_TYPE
                | QUEUE_TYPE
                | STRING_TYPE
                | ENUM_TYPE
                | VAR
                | LIST_TYPE
                | MAP_TYPE
                | SET_TYPE
                | DYNAMIC_TYPE
    '''
    
def p_modifier(p):
    ''' modifier : LATE
                | FINAL
                | CONST
                | 
    '''
    
def p_nullable(p):
    ''' nullable : QUESTION_MARK
                |
    '''

def p_value(p):
 '''value : INTEGER
         | DOUBLE
         | STRING
         | BOOLEAN
         | list
 '''

def p_values(p):
 ''' values : value
             | value COMMA values
 '''
def p_function(p):
    '''
    function : FUNCTION IDENTIFIER LPAREN params RPAREN LBRACE statements RBRACE
    '''
def p_list(p):
    '''
    list : LSQUARE RSQUARE
         | LSQUARE values RSQUARE
    '''  
def p_parameters(p):
      '''
      parameters : parameter
                 | parameter COMMA parameters
                 |
      '''
def p_parameter(p):
  '''
  parameter : type VAR
  '''
def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                 | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    '''
def p_expression(p):
      '''
      expression : expression comparator expression
      | value
      '''
def p_comparator(p):
      '''
      comparator : EQUAL
                 | NOT_EQUAL
                 | LESS
                 | LESS_EQUAL
                 | GREATER
                 | GREATER_EQUAL
      '''

# Error rule for syntax errors
def p_error(p):
   print("Syntax error in input!")

# Build the parser
parser = sint.yacc()

while True:
  try:
      s = input('Ingrese código: ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  if result != None :
     print(result)