import ply.yacc as sint
from lexico import tokens

def p_statement(p):
 '''
 statement : assignment
           | print
 '''

def p_assignment(p):
 '''  assignment : IDENTIFIER ASSIGN value SEMICOLON
 '''

def p_print(p):
 '''  print : PRINT LPAREN values RPAREN SEMICOLON
 '''

def p_value(p):
 '''value : INTEGER
         | DOUBLE
         | STRING
         | BOOLEAN
 '''
def p_values(p):
 ''' values : value
             | value COMMA values 
 '''
# Error rule for syntax errors
def p_error(p):
   print("Syntax error in input!")

# Build the parser
parser = sint.yacc()

while True:
  try:
      s = input('Ingrese codigo: ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  if result != None :
     print(result)