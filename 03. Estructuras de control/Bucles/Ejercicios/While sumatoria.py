acum = 0
cuantos = int(input("¿Cuantos numeros desea ingresar?: "))
ciclo = 0

while ciclo < cuantos:
    num = int(input("Ingrese un numero: "))
    acum += num # La variable acum con valor 0, le agregar el valor de num en cada ciclo. Siendo la sumatoria.
    ciclo += 1 # HASTA QUE LLEGUE AL NUMERO DEL VALOR CUANTOS, PARA EL CICLO E IMPRIME LA SUMATORIA
print("Total: ",acum) # IMPRIME LA SUMATORIA.