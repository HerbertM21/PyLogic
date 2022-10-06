cadena = "piogram"
for variable in cadena:
    print("Hola") #ENTREGA LOS CICLOS DEPENDIENDO DEL NUMERO DE CARACETERES DE LA CADENA.

cadena = "piogram"
for variable in cadena:
    print(variable) #ENTREGA LOS CICLOS CON CADA CARACTER DE LA CADENA.

cadena = input("Ingrese una cadena: ").lower() #CONVIERTE LA PALBRA INGRESADA EN MINUSCULAS.
for variable in cadena:
    if variable in "aeo":
        print(variable) #ENTREGA LOS CARECTERES A, E u O DE LA PALABRA QUE INGRESE.
