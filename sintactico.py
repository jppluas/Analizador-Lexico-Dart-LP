import ply.yacc as sint
from lexico import tokens

def p_statement(p):
    '''
    statement : expression
              | assignment
              | print
              | function
              | if_statement
              | while_statement
              | for_statement
              | lines
              | LBRACE lines RBRACE
              | 
    '''
def p_assignment(p):
    '''  assignment : modifier type nullable IDENTIFIER ASSIGN expression SEMICOLON
                    | type nullable IDENTIFIER ASSIGN expression SEMICOLON
                    | modifier type IDENTIFIER ASSIGN expression SEMICOLON
                    | type IDENTIFIER ASSIGN expression SEMICOLON
    '''

def p_nullable(p):
    ''' nullable : QUESTION_MARK
    '''
    
def p_modifier(p):
    ''' modifier : LATE
                | FINAL
                | CONST
    '''

def p_print(p):
    '''  print : PRINT LPAREN expression RPAREN SEMICOLON
                | PRINT LPAREN RPAREN SEMICOLON
    '''

def p_if_statement(p):
    '''
    if_statement : IF LPAREN logic RPAREN LBRACE lines RBRACE
                 | if_statement ELSE if_statement
                 | if_statement ELSE LBRACE lines RBRACE
    '''


def p_function_call(p):
    '''
    function_call : IDENTIFIER LPAREN parameters RPAREN SEMICOLON
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
            | VOID

    '''

def p_expression(p):
    '''  expression : arithmetic
                    | logic
                    | function_call
    '''

def p_arithmetic(p):
    ''' arithmetic : value
        |   arithmetic arith_op arithmetic
        |   LPAREN arithmetic arith_op arithmetic RPAREN
    '''

def p_comparison(p):
    ''' comparison : value
        |   boolean
        |   comparison comp_op comparison
        |   LPAREN comparison comp_op comparison RPAREN
    '''
    
def p_logic(p):
    ''' logic : comparison
        |   logic logic_op logic
        |   LPAREN logic logic_op logic RPAREN
        |   LOGICAL_NOT logic
    '''

def p_logic_op(p):
    ''' logic_op : LOGICAL_AND
        |   LOGICAL_OR
    '''

def p_arith_op(p):
    ''' arith_op : PLUS
        |   MINUS
        |   TIMES
        |   DIVIDE
    '''

def p_comp_op(p):
      '''
      comp_op : EQUAL
                 | NOT_EQUAL
                 | LESS
                 | LESS_EQUAL
                 | GREATER
                 | GREATER_EQUAL
      '''


def p_values(p):
 ''' values : value
             | value COMMA values
 '''

def p_value(p):
 '''value : IDENTIFIER
         | number
         | string
         | list
 '''
 
def p_number(p):
    ''' number : INTEGER 
                | DOUBLE
     '''
     
def p_string(p):
    ''' string : STRING
    '''
 
def p_boolean(p):
    ''' boolean : TRUE
                | FALSE
    '''

def p_list(p):
    ''' list : LSQUARE RSQUARE
            | LSQUARE values RSQUARE
    
    '''

def p_function(p):
    '''
    function : type IDENTIFIER LPAREN parameters RPAREN LBRACE lines RBRACE
    '''

def p_lines(p):
    ''' lines : line LINE_BREAK lines
            | line lines
            | line
            | 

    '''

def p_line(p):
    ''' line : print
            | assignment
            | function
            | if_statement
    '''

def p_parameters(p):
      '''
      parameters : VOID
                 | parameter
                 | parameter COMMA parameters
                 |
      '''
      
def p_parameter(p):
  '''
  parameter : type IDENTIFIER
            | IDENTIFIER 
  '''
def p_map(p):
    '''
    map : MAP_TYPE LESS type COMMA type GREATER
        | MAP_TYPE LESS type COMMA type GREATER LSQUARE values RSQUARE
        | MAP_TYPE LESS type COMMA type GREATER LSQUARE RSQUARE
    '''

def p_set(p):
    '''
    set : SET_TYPE LESS type GREATER
        | SET_TYPE LESS type GREATER LSQUARE values RSQUARE
        | SET_TYPE LESS type GREATER LSQUARE RSQUARE
    '''
def p_queue(p):
    '''
    queue : QUEUE_TYPE LESS type GREATER
          | QUEUE_TYPE LESS type GREATER LSQUARE values RSQUARE
          | QUEUE_TYPE LESS type GREATER LSQUARE RSQUARE
    '''
def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN logic RPAREN LBRACE lines RBRACE
    '''


def p_for_statement(p):
    '''
    for_statement : FOR LPAREN assignment SEMICOLON logic SEMICOLON assignment RPAREN LBRACE lines RBRACE
    '''


# Build the parser
parser = sint.yacc()
# ejemplo codigo Juan
ejemplo1= "void main() {\n  var x = 5;\n  var y = 10;\n\n  if (x > 0) {\n    print('x es positivo');\n  } else {\n    print('x no es positivo');\n  }\n\n  while (y > 0) {\n    print('y es $y');\n    y = y - 1;\n  }\n\n  customFunction(x, y);\n}\n\nvoid customFunction(int a, int b) {\n  var result = a + b;\n  print('El resultado de la función es $result');\n}"
result = parser.parse(ejemplo1)
print(result)
'''
while True:
  try:
      s = input('Codigo: ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  if result != None :
     print(result)
'''