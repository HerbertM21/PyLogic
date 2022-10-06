veces = int(input("Ingrese el número de veces: "))
cont = 0
acum = 0
for i in range(veces):
    print("--- Ciclo "+str(i+1)+"---")
    num = int(input("Ingrese un número: "))
    if num % 2==0: # CONDICIÓN PARA NUMERO PAR
        cont+=1 # CUENTA LA CANTIDAD DE NUMEROS PARES EN EL TOTAL DE LOS CICLOS
    else:
        acum+=num # CUENTA LA CANTIDAD DE NUMEROS IMPARES.
print("La cantidad de numeros pares es:", cont)
print("La suma total de numeros impares es", acum)