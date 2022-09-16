def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

try:
    print("=====================================================")
    n = int(input("Escriba el numero que quiere utilizar para la recursión: ")) 
    print("El factorial de", n ,"es:",factorial_recursivo(n))
except (RecursionError, TypeError):
        print("¡No se pueden ingresar números negativos y números demasiado altos!")
finally:
       print("=====================================================")