def decorador(func): #Creamos la función decorador (A) con el argumento func
    def nueva_funcion(): #Creamos la nueva función (C)
        print ("Perro dice:")#Añadimos una modificación a la función (B) dentro de (C)
        func() #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A)
    return nueva_funcion #Para devolver (C)
@decorador #Decoramos la función
def saluda():
    print("Guau!")
saluda()