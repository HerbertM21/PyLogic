Lista = [4, 23, 7, 0, 44, 12, 8, 15]

def Busqueda_Lineal(Valor):
    for Puntero in range(0, len(Lista) - 1):
        if Valor == Lista[Puntero]:
            return Puntero
    return None

def Buscar_Valor(Valor):
    if Busqueda_Lineal(Valor) is None:
        print(f"El valor {Valor} no se encontró.")
    else:
        print(f"El valor {Valor} se encontró.")

print("=== BUSQUEDA LINEAL ===")
print(f"Lista de números: {Lista}")
Valor = int(input("Ingrese el valor que quiere encontrar: "))       
Buscar_Valor(Valor)
print("========================")
