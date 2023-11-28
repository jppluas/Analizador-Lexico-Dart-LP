void main() { \n
  int a = 10; \n
  String b = "Hola mundo"; \n\n

  print("a = $a\n"); \n
  print("b = $b\n"); \n

  int c = a + 1; \n
  print("c = $c\n"); \n
  a++;

  if (a > c) { print("a es mayor que c\n"); \n
  } else { print("a es menor o igual que c\n"); }

  while (a < 100) { print("a = $a\n"); }

  for (int i = 0;; i < 10; i++) { \n
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
