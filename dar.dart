void main() {\n  
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
}