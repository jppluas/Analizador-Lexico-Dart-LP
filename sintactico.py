import ply.yacc as sint
from lexico import tokens
errores = ""
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
              | reassignment
              | 
    '''
def p_assignment(p):
    '''  assignment : modifier type nullable IDENTIFIER ASSIGN expression SEMICOLON
                    | type nullable IDENTIFIER ASSIGN expression SEMICOLON
                    | modifier type IDENTIFIER ASSIGN expression SEMICOLON
                    | type IDENTIFIER ASSIGN expression SEMICOLON
                    | type IDENTIFIER ASSIGN expression
                    | int_assignment
                    | string_assignment
                    | list_assigment
                    | map_assigment
    '''

#Regla semantica para la asignacion de valores enteros y double a variables
def p_int_assignment(p):
    '''  int_assignment :  number_type IDENTIFIER ASSIGN arithmetic SEMICOLON
                    | number_type IDENTIFIER ASSIGN arithmetic
                    | modifier number_type nullable IDENTIFIER ASSIGN NULL SEMICOLON
                    | number_type nullable IDENTIFIER ASSIGN NULL SEMICOLON
                    | modifier number_type nullable IDENTIFIER ASSIGN arithmetic SEMICOLON
                    | number_type nullable IDENTIFIER ASSIGN arithmetic SEMICOLON
                    | modifier number_type IDENTIFIER ASSIGN arithmetic SEMICOLON
                    
    '''

#Regla semantica para la asignacion de strings a variables
def p_string_assignment(p):
    '''  string_assignment : type_string IDENTIFIER ASSIGN concate SEMICOLON
                    | type_string IDENTIFIER ASSIGN concate
                    | modifier type_string nullable IDENTIFIER ASSIGN NULL SEMICOLON
                    | type_string nullable IDENTIFIER ASSIGN NULL SEMICOLON
                    | modifier type_string nullable IDENTIFIER ASSIGN concate SEMICOLON
                    | type_string nullable IDENTIFIER ASSIGN concate SEMICOLON
                    | modifier type_string IDENTIFIER ASSIGN concate SEMICOLON
                  
    '''

def p_number_type(p):
    ''' number_type : INTEGER_TYPE
                        | VAR
                        | DOUBLE_TYPE
    '''

def p_type_string(p):
    ''' type_string : STRING_TYPE
                    | VAR
    '''

def p_reassignment(p):
    '''
        reassignment : IDENTIFIER ASSIGN expression SEMICOLON
                     | IDENTIFIER INLINE_ARITH number SEMICOLON
                     | IDENTIFIER INLINE_ARITH SEMICOLON
                     | IDENTIFIER INLINE_ARITH number
                     | IDENTIFIER INLINE_ARITH
    '''

def p_nullable(p):
    ''' nullable : QUESTION_MARK
    '''
    
def p_modifier(p):
    ''' modifier : FINAL
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
    function_call : IDENTIFIER LPAREN values RPAREN SEMICOLON
                    | IDENTIFIER LPAREN values RPAREN
                    | IDENTIFIER LPAREN RPAREN SEMICOLON
                    | IDENTIFIER LPAREN RPAREN
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
                    | concate
                    | logic
                    | function_call
                    | division
    '''

#Regla semantica para la operacion aritmetica de numeros enteros y double
def p_arithmetic(p):
    ''' arithmetic : number
        |   arithmetic arith_op arithmetic
        |   LPAREN arithmetic arith_op arithmetic RPAREN
        
    '''

#Regla semantica para la operacion de division de numeros enteros y double
def p_division(p):
    '''
    division : number DIVIDE number
    '''

def p_concate(p):
    ''' concate : string
        |   concate PLUS concate
        |   LPAREN concate PLUS concate RPAREN
    '''
"""
def p_comparison(p):
    ''' comparison : values
        |   boolean
        |   comparison comp_op comparison
        |   LPAREN comparison comp_op number comparison
    '''
"""
def p_comparison(p):
    ''' comparison : int_comparison
        |   string_comparison
    '''
#Regla semantica para la comparacion de numeros enteros y double
def p_int_comparison(p):
    ''' int_comparison : boolean
        |   number comp_op number
        |   LPAREN number comp_op number RPAREN
    '''

#Regla semantica para la comparacion de strings
def p_string_comparison(p):
    ''' string_comparison : boolean
        |   string comp_op string
        |   LPAREN string comp_op string RPAREN
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
def p_list_assigment(p):
    ''' list_assigment : IDENTIFIER ASSIGN list SEMICOLON
                | type ASSIGN list SEMICOLON


    '''
def p_function(p):
    '''
    function : type IDENTIFIER LPAREN parameters RPAREN LBRACE lines RBRACE
    '''

def p_lines(p):
    ''' lines : line LINE_BREAK lines
            | line lines
            | line
            | LINE_BREAK
            |

    '''

def p_line(p):
    ''' line : print
            | assignment
            | function
            | if_statement
            | while_statement
            | for_statement
            | function_call
            | reassignment
            
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
        | MAP_TYPE
    '''
def p_map_assignment(p):
    '''
    map_assigment : map IDENTIFIER ASSIGN LBRACE RBRACE SEMICOLON
                |   map IDENTIFIER ASSIGN LBRACE map_values RBRACE SEMICOLON
                |   IDENTIFIER IDENTIFIER ASSIGN LBRACE map_values RBRACE SEMICOLON
                |   IDENTIFIER ASSIGN LBRACE RBRACE SEMICOLON
    '''
def p_values_map(p):
    '''map_values : type COLON type
                 |  type COLON type COMMA map_values
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
    for_statement : FOR LPAREN assignment SEMICOLON logic SEMICOLON reassignment RPAREN LBRACE lines RBRACE
    '''

def p_error(p):
    global errores
    error_message = "Error de sintaxis en la entrada en el token '{}'\n".format(p.value)
    error_message += "Tipo del token: {}\n".format(p.type)
    error_message += "Ubicacion del error - Linea {}, Posicion {}\n".format(p.lineno, p.lexpos)
    errores += error_message
   
def analizar(input_string):
    global errores
    errores = ""  # Reinicia la cadena de errores antes de cada análisis
    parser.parse(input_string)
    return errores



# Build the parser
parser = sint.yacc()

# ejemplo codigo Juan
ejemplo1= '''void main() {\n  
var x = 5;\n  
var y = 10;\n\n  

if (x > 0) {\n    
print('x es positivo');\n  
} else {\n    
print('x no es positivo');\n  
}\n\n  

while (y > 0) {\n    
print('y es $y');\n    
y = y - 1;\n  
}\n\n 

customFunction(x, y); \n }

void customFunction(int a, int b) {\n 
var result = a + b;\n  
print('El resultado de la función es $result');\n
}'''

ejemplo2 = '''
void main() { \n
  int a = 10; \n
  String b = "Hola mundo"; \n\n

  print("a = $a\n"); \n
  print("b = $b\n"); \n

  int c = 2 + 1; \n
  print("c = $c\n"); \n
  a++;

  if (a > c) { print("a es mayor que c\n"); \n
  } else { print("a es menor o igual que c\n"); }

  while (a < 100) { print("a = $a\n"); }

  for (int i = 0; i < 10; i++) { \n
    print("i = $i\n"); \n
  }
\n
saludar(); \n

}

\n
void saludar() { \n
  print("Hola mundo\n"); \n
}
\n

'''


ejemplo3= "7/0"
result = parser.parse(ejemplo3)
if result == None :
     print('PASS')


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