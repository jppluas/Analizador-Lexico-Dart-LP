import ply.yacc as sint
from lexico import tokens

def p_statement(p):
 '''
 statement : assignment
           | print
           | function
           | if_statement
 '''

def p_expression(p):
    '''  expression : value
        |   expression op expression
        |   LPAREN expression op expression RPAREN
    '''
    
def p_assignment(p):
    '''  assignment : modifier type nullable IDENTIFIER ASSIGN expression SEMICOLON
    '''

def p_print(p):
    '''  print : PRINT LPAREN expression RPAREN SEMICOLON
    '''

def p_logical(p):
    ''' logical : LOGICAL_AND
        |   LOGICAL_OR
        |   LOGICAL_NOT
    '''

def p_arithmetic(p):
    ''' arithmetic : PLUS
        |   MINUS
        |   TIMES
        |   DIVIDE
    '''

def p_comparation(p):
      '''
      comparation : EQUAL
                 | NOT_EQUAL
                 | LESS
                 | LESS_EQUAL
                 | GREATER
                 | GREATER_EQUAL
      '''

def p_op(p):
    ''' op : arithmetic
        |   comparation
        |   logical
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
 '''value : IDENTIFIER
         | INTEGER
         | DOUBLE
         | STRING
         | TRUE
         | FALSE
         | list
 '''

def p_values(p):
 ''' values : value
             | value COMMA values
 '''

def p_parameter(p):
  '''
  parameter : type IDENTIFIER
  '''

def p_parameters(p):
      '''
      parameters : parameter
                 | parameter COMMA parameters
                 |
      '''
      
def p_function(p):
    '''
    function : type IDENTIFIER LPAREN parameters RPAREN LBRACE statement RBRACE
    '''
    
def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE statement RBRACE
                 | ELSE if_statement
                 | if_statement ELSE LBRACE statement RBRACE
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