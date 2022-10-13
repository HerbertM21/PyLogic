
# algoritmo de ordenamiento por inserción 
def funcion(li):
    for i in range(1, len(li)): # desde 1 hasta el tamaño de la lista, i
        v = li[i] # el valor actual es el valor de la lista en la posición i
        p = i # la posición actual es la posición i
        while p > 0 and li[p - 1] > v: # mientras la posición actual sea mayor que 0 y el valor de la lista en la posición actual - 1 sea mayor que el valor actual
            li[p] = li[p - 1] # el valor de la lista en la posición actual es el valor de la lista en la posición actual - 1
            p = p - 1 # la posición actual es la posición actual - 1
        li[p] = v # el valor de la lista en la posición actual es el valor actual
        print(li)
    return li  # devolvemos la lista ordenada

if __name__ == "__main__":
    lista = [3, 2, 1, 7, 4] # creamos una lista con los números del 1 al 10
    funcion(lista) # llamamos a la función
    print(lista) # imprimimos la lista

# PASOS DEL ALGORITMO
# 1. i = 1
# 2. v = 2
# 3. p = 1
# 4. p > 0 and li[p - 1] > v
# 5. li[p] = li[p - 1]
# 6. p = p - 1
# 7. p > 0 and li[p - 1] > v
# 8. li[p] = li[p - 1]
# 9. p = p - 1
# 10. p > 0 and li[p - 1] > v
# 11. li[p] = li[p - 1]
# 12. p = p - 1
# 13. p > 0 and li[p - 1] > v
# 14. li[p] = li[p - 1]
# 15. p = p - 1
# 16. p > 0 and li[p - 1] > v
# 17. li[p] = li[p - 1]
# 18. p = p - 1
# 19. p > 0 and li[p - 1] > v
# 20. li[p] = li[p - 1]
# 21. p = p - 1
# 22. p > 0 and li[p - 1] > v
# 23. li[p] = li[p - 1]
# 24. p = p - 1
# 25. p > 0 and li[p - 1] > v
# 26. li[p] = li[p - 1]
# 27. p = p - 1

# 28. p > 0 and li[p - 1] > v
# 29. li[p] = li[p - 1]
# 30. p = p - 1


