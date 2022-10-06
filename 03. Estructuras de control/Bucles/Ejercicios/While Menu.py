# CALCULADORA DE SUMA Y RESTA

opcion = ""
while opcion != 3:
    print("===================================")
    print("BIENVENIDO A NUESTRA CALCULADORA")
    print("MENU DE OPCIONES:")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir de la calculadora")
    print("===================================")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("===================================")
        n = int(input("- Valor A: "))
        m = int(input("- Valor B: "))
        total = n+m
        print("(*) La suma de",n,"y",m,"es ",total)
        print("===================================")
    elif opcion == 2:
        n = int(input("- Valor A: "))
        m = int(input("- Valor B: "))
        total = n-m
        print("(*) La resta de",n,"y",m,"es ",total)
        print("===================================")
    elif opcion == 3:
        print("===================================")
        print("Gracias por entrar a nuestra calculadora.")
        print("===================================")
    else:
        print("Ingrese un valor correcto.")