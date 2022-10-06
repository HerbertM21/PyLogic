def info():
    frutas = ["Manzana", "Naranja", "Uva", "Pera", "Sandia"]
    cantidad = [5, 3, 5, 7, 8]
    clientes = ["Herbert", "Andrés", "Juan", "Ángel", "Pol"]
    precio_peso = [2000, 3500, 1400, 6000, 2050]

    for i in range(len(frutas)): # El len cuenta los objetos de la lista.
        fruta = frutas[i]
        precio = precio_peso[i]
        can = cantidad[i]
        cli = clientes[i]
        if fruta == fruta_input:
            print("======= "+fruta+" =========")
            print("+ Cliente: ",cli)
            print("+ Cantidad: ",can)
            print("+ Precio: ",precio)
            print("=========================")

print("---- Información de compras ----")
fruta_input = str(input("Ingrese la fruta para recibir informacion: "))
info()