Lista = [2, 41, 25, 23, 14, 29, 0, 1, 18, 7, 11, 99, 34]
Lista.sort() # Se necesita dicha función para saber si buscar para adelante o atrás en lista ordenada-

def Busqueda_Binaria(valor):
    Inicio = 0
    Fin = len(Lista) - 1
    while Inicio <= Fin:
        puntero = (Inicio + Fin) // 2
        if valor == Lista[puntero]:
            return puntero
        elif valor > Lista[puntero]:
            Inicio = puntero + 1
        else:
            Fin = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = Busqueda_Binaria(valor)
    if res_busqueda is None:
        print(f"+ Resultado: El número {valor} no se encuentró")
    else:
        print(f"+ Resultado: El número {valor} se encontró en la posición {res_busqueda}") 

print("=== BUSQUEDA BINARIA ===")
print(f"Lista de números: {Lista}")
valor = int(input("Ingrese el valor que quiere encontrar: "))       
buscar_valor(valor)
print("========================")