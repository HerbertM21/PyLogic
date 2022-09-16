def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

n = int(input("Escriba el numero que quiere utilizar para la recursión: "))
print("El factorial de", n ,"es:",factorial_recursivo(n))
print("La serie fibonacci de", n ,"es:",fibonacci_recursivo(n))