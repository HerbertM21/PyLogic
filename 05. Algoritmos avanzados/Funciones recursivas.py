def factorial_recursivo(n): # 5! = 5 * 4 * 3 * 2 * 1
    if n == 1: # Caso base
        return 1 # 1! = 1
    else: # Caso recursivo
        return n * factorial_recursivo(n-1) # n! = n * (n-1)!

def fibonacci_recursivo(n): # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    if n == 0: # Caso base
        return 0 # 0
    elif n == 1: # Caso base
        return 1 # 1
    else: # Caso recursivo
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2) # n = n-1 + n-2

n = int(input("Escriba el numero que quiere utilizar para la recursión: ")) # 5
print("El factorial de", n ,"es:",factorial_recursivo(n)) # 5! = 5 * 4 * 3 * 2 * 1
print("La serie fibonacci de", n ,"es:",fibonacci_recursivo(n)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...