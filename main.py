import ply.lex as lex


# Construir el analizador léxico
lexer = lex.lex()

tokens = (
  'IDENTIFIER',
  'NUMBER',
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
  'BOOLEAN',
  'NULL',
  'KEYWORD',
  'COMMENT',
  'BLOCKCOMMENT'
    
    
    )

keywords = {
  'var': 'VAR',
  'int': 'INT',
  'double': 'DOUBLE',
  'String': 'STRING_TYPE',
  'bool': 'BOOLEAN_TYPE',
  'true': 'BOOLEAN',
  'false': 'BOOLEAN',
  'null': 'NULL',
  'if': 'IF',
  'else': 'ELSE',
  'while': 'WHILE'
  }

tokens += tuple(keywords.values())


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'


def t_NUMBER(t):
  r'\d+(\.\d+)?'
  t.value = float(t.value) if '.' in t.value else int(t.value)
  return t


def t_STRING(t):
  r'\"(\\.|[^"])*\"'
  t.value = t.value[1:-1]  # Eliminar comillas
  return t


def t_COMMENT(t):
  r'//.*'
  pass


def t_BLOCKCOMMENT(t):
  r'/\*(.|\n)*?\*/'
  pass

# Ejemplo de entrada
input_text = """
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
"""input_text = 
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
# Configurar el analizador léxico con la entrada
lexer.input(input_text)

# Procesar la entrada y mostrar los tokens
for token in lexer:
  print(f'Token: {token.type}, Valor: {token.value}')
