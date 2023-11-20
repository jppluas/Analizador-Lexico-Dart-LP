import ply.lex as lex

tokens = (
  #Aporte de Juan Gallo
  'IDENTIFIER',
  'INTEGER',
  'DOUBLE',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'LBRACE',
  'RBRACE',
  'SEMICOLON',
  'STRING',
  'KEYWORD',
  'COMMENT',
  'BLOCKCOMMENT',
  #Aporte de Juan Pablo Plúas
  'ASSIGN',
  'EQUAL',
  'NOT_EQUAL',
  'GREATER',
  'LESS',
  'GREATER_EQUAL',
  'LESS_EQUAL',
  'COLON',
  'COMMA',
  'LSQUARE',
  'RSQUARE',
  'DOT',
  'LOGICAL_AND',
  'LOGICAL_OR', 
  'LOGICAL_NOT',
  'QUESTION_MARK',
  'LINE_BREAK',
  'INLINE_ARITH'
  )

keywords = {
  #Aporte de Juan Gallo
  'var': 'VAR',
  'int': 'INTEGER_TYPE',
  'double': 'DOUBLE_TYPE',
  'String': 'STRING_TYPE',
  'bool': 'BOOLEAN_TYPE',
  'dynamic': 'DYNAMIC_TYPE',
  'List': 'LIST_TYPE',
  'Map': 'MAP_TYPE',
  'Set': 'SET_TYPE',
  'Queue' : 'QUEUE_TYPE',
  'enmu' : 'ENUM_TYPE',
  'true': 'TRUE',
  'false': 'FALSE',
  'null': 'NULL',
  'if': 'IF',
  'else': 'ELSE',
  'while': 'WHILE',
  'for': 'FOR',
  'return': 'RETURN',
  'switch': 'SWITCH',
  'case': 'CASE',
  'break': 'BREAK',
  'continue': 'CONTINUE',
  'try': 'TRY',
  'catch': 'CATCH',
  'finally': 'FINALLY',
  'throw': 'THROW',
  'abstract': 'ABSTRACT',
  'implements': 'IMPLEMENTS',
  'show': 'SHOW',
  'as': 'AS',
  'print' : 'PRINT',
  #Aporte de Juan Pablo Plúas
  'final' : 'FINAL',
  'const' : 'CONST',
  'import': 'IMPORT',
  'static': 'STATIC',
  'assert': 'ASSERT',
  'enum': 'ENUM',
  'in': 'IN',
  'super': 'SUPER',
  'async': 'ASYNC',
  'export': 'EXPORT',
  'interface': 'INTERFACE',
  'await': 'AWAIT',
  'extends': 'EXTENDS',
  'is': 'IS',
  'sync': 'SYNC',
  'external': 'EXTERNAL',
  'library': 'LIBRARY',
  'on': 'ON',
  'typedef': 'TYPEDEF',
  'default': 'DEFAULT',
  'get': 'GET',
  'rethrow': 'RETHROW',
  'deferred': 'DEFERRED',
  'hide': 'HIDE',
  'do': 'DO',
  'set': 'SET',
  'yield': 'YIELD',
  'extension': 'EXTENSION',
  'late': 'LATE',
  'operator': 'OPERATOR',
  'part': 'PART',
  'with': 'WITH',
  'void': 'VOID'
}

tokens += tuple(keywords.values())

#Aporte de Juan Gallo
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
#Aporte de Juan Pablo Plúas
t_COMMA = r',' 
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_DOT = r'\.'
t_ASSIGN = r'='
t_EQUAL  = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'\>'
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_LOGICAL_AND = r'\&\&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'\!'
t_QUESTION_MARK = r'\?'
t_LINE_BREAK = r'(\\n)+'

#Aporte de Juan Pablo Plúas

def t_INLINE_ARITH(t):
    r'(([\+\-\*\/]\=)|(\+\+|\-\-))'
    return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#Aporte de Juan Gallo
def t_STRING(t):
  r'[\"\'](\\.|[^\"\'])*[\"\']' #Acepta comillas simples o dobles
  t.value = t.value[1:-1]  # Eliminar comillas
  return t

def t_VOID(t):
    r'void'
    return t
    
def t_WHILE(t):
    r'while'
    return t
def t_COMMENT(t):
  r'//.*'
  pass

def t_BLOCKCOMMENT(t):
  r'/\*(.|\n)*?\*/'
  pass

def t_IDENTIFIER(t):
  r'[a-zA-Z_][a-zA-Z0-9_\'"]*'
  t.type = keywords.get(t.value, 'IDENTIFIER')
  return t


# Ignorar caracteres en blanco y saltos de línea
t_ignore = ' \t\n'

# Función de manejo de errores
def t_error(t):
  print(f"Carácter ilegal: {t.value[0]}")
  t.lexer.skip(1)

# codigo de prueba Juan Pablo Plúas
input_text1 = """
void main() {
  var x = 5;
  var y = 10.5;
  var name = "Alice";
  var isActive = true;

  if (x > 0) {
    print("x is positive");
  } else {
    print("x is non-positive");
  }

  var myList = [1, 2, 3, 4];
  var myMap = {'a': 1, 'b': 2, 'c': 3};

  for (var item in myList) {
    print(item);
  }

  print('Map entries: $myMap');

  // This is a single-line comment

  /*
    This is a
    multi-line comment
  */

  var calculation = x * y / 2;
  print('Calculation: $calculation');
}
"""
# codigo de prueba Juan Gallo
input_text2 = """
int main() {
    var x = 42;
    double y = 3.14;
    String hello = "Hello, World!";
    bool isTrue = true;
    if (isTrue) {
        print(hello);
    } else {
        print("Not true");
    }
    return null;

    // Operadores y literales de colección
    var list = [1, 2, 3];
    var set = {'apple', 'banana'};
    var map = {'name': 'Alice', 'age': 30};

    // Comentarios de bloque
    /* Este es un comentario de bloque */
}
"""


# Construir el analizador léxico
lexer = lex.lex()

# Configurar el analizador léxico con la entrada
#lexer.input(input_text2)

# Procesar la entrada y mostrar los tokens
#for token in lexer:
#  print(f'Token: {token.type}, Valor: {token.value}')
