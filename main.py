import ply.lex as lex


# Construir el analizador léxico
lexer = lex.lex()

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

# Configurar el analizador léxico con la entrada
lexer.input(input_text)

# Procesar la entrada y mostrar los tokens
for token in lexer:
  print(f'Token: {token.type}, Valor: {token.value}')
