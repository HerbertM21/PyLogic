# Analisis de frecuencia de caracteres de un archivo de texto
# Autor: Herbert Mayorga - IECI
# Fecha: 23-10-2022

# 1. Una funcion llamada lectura(), que lea el archivo de texto y determine la frecuencia de cada caracter contenido en el texto. La funcion debe retornar una lista con la informacion del caracter y su frecuencia.
# 2. Una funcion que reciba la lista de la funcion lectura() y la retorne ordenada de menor a mayor de acuerdo a la frecuencia de los caracteres.
# 3. Una funcion que reciba la lista ordenada de la funcion anterior e imprima el caracter y su frecuencia.
# 4. Una funcion que reciba la lista ordenada y genere un archivo de salida conteniendo el caracter, un espacio en blanco y su frecuencia, una linea por cada caracter.
# 5. El programa principal debe pedir al usuario el nombre del archivo de texto a analizar

# FUNCION N1
def reading(archivo):
    with open(archivo, "r") as f:
        texto = f.read() 
        lista = {} 
        
        # Dentro del diccionario, se asigna la key como el caracter y el valor como la frecuencia
        # Dentro del bucle se recorre el texto y se le asigna el numero de veces que se repite la key
        # Por lo cual, al momento de llamar a "Lista[caracter] en otra funcion, solamente se obtiene el valor de la key"
        
        for caracter in texto: # Recorremos el texto del archivo
            if caracter in lista: 
                lista[caracter] += 1 # Sumamos 1 a la frecuencia del caracter
            else:
                lista[caracter] = 1 # Si no, agregamos el caracter a la lista y le asignamos una frecuencia de 1
    return lista

# FUNCION N2
def sort(lista):
    listSort = []
    # Agregamos a la lista ordenada el caracter y su frecuencia:
    for caracter in lista:
        listSort.append([caracter, lista[caracter]]) 
    # Ordenamiento de menor a mayor con bubble sort:
    for i in range(len(listSort)): 
        for j in range(len(listSort) - 1):
            if listSort[j][1] > listSort[j + 1][1]:
                listSort[j], listSort[j + 1] = listSort[j + 1], listSort[j]
    return listSort

# FUNCION N3
def consoleLog(listSort):
    # Se imprime en la consola el caracter y su frecuencia (Funcion innecesaria)
    for caracter in listSort:
        print(f"\n Caracter: {caracter[0]} = {str(caracter[1])}")

# FUNCION N4
def output(listSort):
    # Se crea un archivo de salida con el caracter y su frecuencia
    output = input("Ingrese el nombre del archivo de salida: ")
    # Abrimos el archivo de salida en modo escritura:
    with open(output, "w") as f: 
        f.write("Autor: Herbert Mayorga - IECI \n")
        for caracter in listSort:
            f.write(f".- Caracter: {caracter[0]} = {str(caracter[1])} \n")

# PROGRAMA PRINCIPAL
def main():
    print("----------------------------------------------------------")
    print("Analisis de frecuencia de caracteres de un archivo de texto")
    print("----------------------------------------------------------")
    
    # Capturamos los posibles errores dentro del programa prinicipal:
    try:
        archivo = input("Ingrese el nombre del archivo de texto: ")
        lista = reading(archivo)
        listSort = sort(lista)
        consoleLog(listSort)
        output(listSort)
    except (FileNotFoundError, TypeError):
        print("Lo lamentamos, el archivo no existe.")
        
if __name__ == "__main__":
    main()