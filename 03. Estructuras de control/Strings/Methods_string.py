string = "Herbert Mayorga"

#Lista de metodos para strings
print(dir(string))
# Devuelve la longitud de la cadena de caracteres.
print(len(string)) #15
# Devuelve el numero de veces que se repite un caracter.
print(string.count("e")) #2 veces e
# Convertir la string en mayusculas
print(string.upper())
# Convertir la string en Minusculas
print(string.lower())
# Convertir el primer caracter en mayusculas
print(string.capitalize())
# Convertir el primer caracter de cada palabra en mayusculas
print(string.title())
# Reemplazar una palabra del string
print(string.replace("Mayorga","Mansilla")) # Herbert Mansilla
# string alternando mayus y minus.
print(string.swapcase())
# CONCATENAR LA VARIABLE DENTRO DEL STRING MEDIANTE EL METODO .FORMAT
print("My name is {0}".format(string))
# Permitir que la variable se concantene dentro de las comillas.
print(f"Hola {string}")
# Separar string mediante un indicador de parametro.
print(string.split(' ')) # ['Herbert', 'Mayorga']
