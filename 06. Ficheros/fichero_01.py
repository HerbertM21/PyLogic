# Funciones básicas de ficheros.abs(
# Autor: Herbert Mayorga Mansilla

# Abrir un fichero en modo lectura
fichero = open("fichero.txt", "r")

# Leer el contenido del fichero
contenido = fichero.read()

# Mostrar el contenido del fichero
print(contenido)

# Cerrar el fichero
fichero.close()

# Abrir un fichero en modo escritura
fichero = open("fichero.txt", "w")

# Escribir en el fichero
fichero.write("Hola mundo")

# Cerrar el fichero
fichero.close()

# Abrir un fichero en modo lectura y escritura
fichero = open("fichero.txt", "r+")



# Se usa with para abrir el fichero y cerrarlo automáticamente.
with open('06. Ficheros/texto.txt', 'r') as f: # Se abre el fichero en modo lectura.
    print(f.read()) # Se lee el fichero.

print("...............") 

with open('06. Ficheros/texto.txt', 'r') as f: # Se abre el fichero en modo lectura.
    print(f.readline()) # Se lee una línea del fichero.
    print(f.readline()) # Se lee otra línea del fichero.