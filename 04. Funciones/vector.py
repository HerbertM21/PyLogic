# calculadora de vectores con funciones

import math

def decorador(funcion):
    def funcion_decorada(*args): 
        print("\t* ============== Nuevo vector ===================")
        resultado = funcion(*args) 
        return resultado 
    return funcion_decorada 

@decorador 
def pedir_vector():
    x = float(input(f'1. Introduce la coordenada x: '))
    y = float(input(f'2. Introduce la coordenada y: '))
    z = float(input(f'3. Introduce la coordenada z: '))
    return [x, y, z]

def menu():
        print("\t* ============== MENU ===================")
        print("1.- SUMA DE VECTORES  2.- RESTA DE VECTORES  3.- PRODUCTO ESCALAR  4.- NORMA DE VECTORES  5.- SALIR")
        respuesta = int(input(">>> "))

        if respuesta == 1:
            print("===========================================")
            print("SUMA DE VECTORES")
            print("===========================================")
            print("1.- V1 + V2  2.- V1 + V3  3.- V2 + V3  4.- V1 + V2 + V3")
            respuesta = int(input(">>> "))
            if respuesta == 1:
                print("===========================================")
                print("V1 + V2 = ", suma(v1, v2))
                print("===========================================")
            elif respuesta == 2:
                print("===========================================")
                print("V1 + V3 = ", suma(v1, v3))
                print("===========================================")
            elif respuesta == 3:
                print("===========================================")
                print("V2 + V3 = ", suma(v2, v3))
                print("===========================================")
            elif respuesta == 4:
                print("===========================================")
                print("V1 + V2 + V3 = ", suma(v1, v2, v3))
                print("===========================================")
            else:
                print("Selecciona una opción correcta, por favor")

        elif respuesta == 2:
            print("===========================================")
            print("RESTA DE VECTORES")
            print("===========================================")
            print("1.- V1 - V2  2.- V1 - V3  3.- V2 - V3  4.- V1 - V2 - V3")
            respuesta = int(input(">>> "))
            if respuesta == 1:
                print("===========================================")
                print("V1 - V2 = ", resta(v1, v2))
                print("===========================================")
            elif respuesta == 2:
                print("===========================================")
                print("V1 - V3 = ", resta(v1, v3))
                print("===========================================")
            elif respuesta == 3:
                print("===========================================")
                print("V2 - V3 = ", resta(v2, v3))

            elif respuesta == 4:
                print("===========================================")
                print("V1 - V2 - V3 = ", resta(v1, v2, v3))
                print("===========================================")

            else:
                print("Selecciona una opción correcta, por favor")

        elif respuesta == 3:
            print("===========================================")
            print("PRODUCTO ESCALAR")
            print("===========================================")
            print("1.- V1 * V2  2.- V1 * V3  3.- V2 * V3  4.- V1 * V2 * V3")
            respuesta = int(input(">>> "))
            if respuesta == 1:
                print("===========================================")
                print("V1 * V2 = ", producto_escalar(v1, v2))
                print("===========================================")
            elif respuesta == 2:
                print("===========================================")
                print("V1 * V3 = ", producto_escalar(v1, v3))
                print("===========================================")
            elif respuesta == 3:
                print("===========================================")
                print("V2 * V3 = ", producto_escalar(v2, v3))
                print("===========================================")
            elif respuesta == 4:
                print("===========================================")
                print("V1 * V2 * V3 = ", producto_escalar(v1, v2, v3))
                print("===========================================")
            else:
                print("Selecciona una opción correcta, por favor")

        elif respuesta == 4:

            print("===========================================")
            print("NORMA DE VECTORES")
            print("===========================================")
            print("1.- |V1|  2.- |V2|  3.- |V3|  4.- |V1| + |V2| + |V3|")
            respuesta = int(input(">>> "))
            if respuesta == 1:
                print("===========================================")
                print("|V1| = ", norma(v1))
                print("===========================================")
            elif respuesta == 2:
                print("===========================================")
                print("|V2| = ", norma(v2))
                print("===========================================")
            elif respuesta == 3:
                print("===========================================")
                print("|V3| = ", norma(v3))
                print("===========================================")
            elif respuesta == 4:
                print("===========================================")
                print("|V1| + |V2| + |V3| = ", norma(v1, v2, v3))
                print("===========================================")
            else:
                print("Selecciona una opción correcta, por favor")

        elif respuesta == 5:

            print("===========================================")
            print("SALIR")
            print("===========================================")

        else:
            print("Selecciona una opción correcta, por favor")

def suma(*args): # *args para permitir cualquier numero de parametros para la función.
    resultado = [0, 0, 0] # inicializamos el resultado a 0
    for vector in args: # para cada vector en la tupla de argumentos
        for i in range(3): # para cada componente del vector
            resultado[i] += vector[i] # sumamos la componente del vector al resultado
    return resultado # devolvemos el resultado
    
def resta(*args): # *args para permitir cualquier numero de parametros para la función.
    resultado = [0, 0, 0] # inicializamos el resultado a 0
    for vector in args: # para cada vector en la tupla de argumentos
        for i in range(3): # para cada componente del vector
            resultado[i] -= vector[i] # restamos la componente del vector al resultado
    return resultado # devolvemos el resultado

def producto_escalar(*args): # *args para permitir cualquier numero de parametros para la función.
    resultado = 0 # inicializamos el resultado a 0
    for vector in args: # para cada vector en la tupla de argumentos
        for i in range(3): # para cada componente del vector
            resultado += vector[i] # sumamos la componente del vector al resultado
    return resultado # devolvemos el resultado

def norma(*args): # *args para permitir cualquier numero de parametros para la función.
    resultado = 0 # inicializamos el resultado a 0
    for vector in args: # para cada vector en la tupla de argumentos
        for i in range(3): # para cada componente del vector
            resultado += vector[i]**2 # sumamos la componente del vector al resultado
    return resultado**0.5 # devolvemos el resultado

if __name__ == "__main__":
    v1 = pedir_vector()
    v2 = pedir_vector()
    v3 = pedir_vector()
    menu()