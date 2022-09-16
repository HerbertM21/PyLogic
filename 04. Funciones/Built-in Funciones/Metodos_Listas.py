Lista2 = ["Herbert", "Mayorga", "Mansilla"]
Lista = [2, 4, 53, 22, 42, 22]
Lista_Nueva = [24, 33, 12, 5]


# Añade un elemento a la lista al final de la lista
Lista.append(10) 
print(Lista) # [2, 4, 53, 22, 42, 10]
# Añade varios elementos al final de la lista
Lista.extend(Lista_Nueva) 
print(Lista) # [2, 4, 53, 22, 42, 10, 24, 33, 12, 5]
# Añade un elemento en una posición determinada. (Posición, elemento)
Lista.insert(2, 3)
print(Lista) # [2, 4, 3, 53, 22, 42, 10, 24, 33, 12, 5]


# Ordenar una lista en reversa (invertir orden)
Lista.reverse()
print(Lista)
# Ordenar una lista en forma ascendente ( Ordenada )
Lista.sort()
print(Lista)
# Ordenar una lista en forma descendente
Lista.sort(reverse = True)
print(Lista)


# Obtener el numero de indice de un elemento.
print(Lista.index(53,0, 10)) # 3
# Obtener la cantidad de elementos que se repite
print(Lista.count(22)) # 2


# Eliminar un elemento por su valor
Lista.remove(4)
print(Lista) # [2, 3, 53, 22, 42, 22, 10, 24, 33, 12, 5]
# Eliminar el último elemento de la lista
Lista.pop()
print(Lista) # [2, 3, 53, 22, 42, 22, 10, 24, 33, 12]
# Eliminar un elemento por su índice
Lista.pop(3)
print(Lista) # [2, 3, 53, 42, 22, 10, 24, 33, 12]

