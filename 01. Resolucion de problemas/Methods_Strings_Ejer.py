
# Variables
N = int(input("Introduce un numero menor de 100: "))
suma = 0
i = 0
while i < N: 
    if i % 4 == 0:
        suma += i**2
    i += 1
print("La suma de los cuadrados de los numeros que estan separados entre si cuatro posiciones es: ", suma)

