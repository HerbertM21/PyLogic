def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

n = int(input("Escriba el numero que quiere utilizar para la recursión: "))
print("La serie fibonacci de", n,"es:",fibonacci_recursivo(n))
