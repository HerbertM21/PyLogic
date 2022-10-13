import random

cantidad = int(input("Cuantos lanzamientos se hicieron? "))
resultados = [] # Creamos una lista vacia
# i = 0 hasta cantidad - 1
for i in range(cantidad): # Creamos un bucle que se repita la cantidad de veces que se ingresaron
    # Crear un resultado aleatorio entre S y C (S = sol, C = cruz) para la variable resultado
    resultado = random.choice(["S", "C"]) # Creamos una variable que guarde un resultado aleatorio entre S y C
    if resultado == "C" or resultado == "S": # Si el resultado es C o S
        resultados.append(resultado) # Agregamos el resultado a la lista
        print(resultados[i]) # Imprimimos la lista
    else:
        print("Resultado invalido")
        break

# i = 0 hasta cantidad - 4
for i in range(cantidad - 3): # Creamos un bucle que se repita la cantidad de veces que se ingresaron - 3
    if resultados[i] != resultados[i + 1] and resultados[i + 1] != resultados[i + 2] and resultados[i + 2] != resultados[i + 3]: # Si el resultado es diferente al siguiente y el siguiente es diferente al siguiente del siguiente y el siguiente del siguiente es diferente al siguiente del siguiente del siguiente
        print("El jugador gano") # El jugador gano
        break
    elif resultados[i] == resultados[i + 1] == resultados[i + 2] == resultados[i + 3]: # Si no
        print("El jugador perdio") # El jugador perdio
        break