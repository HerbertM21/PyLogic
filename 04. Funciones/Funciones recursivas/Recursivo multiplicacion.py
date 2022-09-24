# multiplicar sin usar el operador *

def multiplicar(a, b): # 5 * 3 = 5 + 5 + 5
    if b == 0: # Caso base
        return 0 # 0 * 5 = 0
    else: # Caso recursivo
        return a + multiplicar(a, b-1)

# Explicar la recursividad de multiplicacion de 5 * 3
# 5 * 3 = 5 + 5 + 5
# 5 * 2 = 5 + 5
# 5 * 1 = 5
# https://www.youtube.com/watch?v=n73iZl4cK2Y&ab_channel=UnicornioRecursivo
print(multiplicar(5, 3)) # 5 * 3 = 5 + 5 + 5

