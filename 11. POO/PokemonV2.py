from Modulos.Utilidades import tirar_dado

class Pokemon:
    def __init__(self, nombre, ataque, tipo):
        self.nombre = nombre
        self.ataque = float(ataque)
        self.tipo = tipo
        self.vida = 100

    def gano(self):
        print(f"\n=={self.nombre}== GANO LA BATALLA.\n")

    def dmg(self, var):
        if "agua" == self.tipo and "fuego" == var.tipo:
            self.ataque *= 2.0
            return self.ataque
        elif "agua" == self.tipo and "tierra" == var.tipo:
            self.ataque *= 1.5
            return self.ataque
        elif "electrico" == self.tipo and "agua" == var.tipo:
            self.ataque *= 2.0
            return self.ataque
        elif "electrico" == self.tipo and "tierra" == var.tipo:
            self.ataque *= 0.5
            return self.ataque
        elif "fuego" == self.tipo and "planta" == var.tipo:
            self.ataque *= 2.0
            return self.ataque
        elif "fuego" == self.tipo and "tierra" == var.tipo:
            self.ataque *= 0.5
            return self.ataque
        else:
            self.ataque *= 1

#Creamos nuestros pokemons
p1 = Pokemon("Pikachu", 35, "electrico")
p2 = Pokemon("Charizard", 35, "fuego")
p3 = Pokemon("Blastoise", 35, "agua")
p4 = Pokemon("Bulbasaur", 35, "planta")
p5 = Pokemon("Onix", 35, "tierra")

while True:
#Creamos los valores de vida
    p1.vida = 100
    p2.vida = 100
    p3.vida = 100
    p4.vida = 100
    p5.vida = 100
#Creamos variables de daño
    p1.ataque = 35
    p2.ataque = 35
    p3.ataque = 35
    p4.ataque = 35
    p5.ataque = 35
#Elegimos el turno de los jugadores
    turno = tirar_dado(2)
    print("----0----\nBienvenido al juego de Pokemon.\n----0----")
#El jugador 1 elige su pokemon
    while True:
        print(f"Estos son los pokemon disponibles:\n{p1.nombre} -> 0\n{p2.nombre} -> 1")
        print(f"{p3.nombre} -> 2\n{p4.nombre} -> 3\n{p5.nombre} -> 4\n")
        elec1 = int(input("El jugador 1 elige un pokemon: \n> "))
        pok1 = elec1
        if pok1 == 0:
            pok1 = p1
            break
        elif pok1 == 1:
            pok1 = p2
            break
        elif pok1 == 2:
            pok1 = p3
            break
        elif pok1 == 3:
            pok1 = p4
            break
        elif pok1 == 4:
            pok1 = p5
            break
        else:
            print("El pokemon no existe")
    print(f"El jugador 1 ha elegido a {pok1.nombre}.\n----0----")

#El jugador 2 elige su pokemon
    while True:
        elec2 = int(input("El jugador 2 elige un pokemon: \n> "))
        pok2 = elec2
        if elec1 == elec2:
            print("No puedes utilizar el mismo pokemon que tu rival.")
        else:
            if pok2 == 0:
                pok2 = p1
                break
            elif pok2 == 1:
                pok2 = p2
                break
            elif pok2 == 2:
                pok2 = p3
                break
            elif pok2 == 3:
                pok2 = p4
                break
            elif pok2 == 4:
                pok2 = p5
                break
            else:
                print("El pokemon no existe")
    print(f"El jugador 2 ha elegido a {pok2.nombre}.\n----0----")

    print("La batalla está apunto de empezar")
    print(f"{pok1.nombre} se enfrenta a {pok2.nombre}.\n")
# Definimos el ataque de los jugadores.
    pok1.dmg(pok2)
    pok2.dmg(pok1)
    print(f"El daño de {pok1.nombre} es de {pok1.ataque}")
    print(f"El daño de {pok2.nombre} es de {pok2.ataque}")
    print("\n==LA PRIMERA RONDA COMIENZA==\n")


    while pok1.vida > 0 and pok2.vida > 0:
        if  turno == 1:
            pok2.vida = pok2.vida - pok1.ataque
            turno = 2
            if pok2.vida <= 0:
                print(f"{pok1.nombre} ataca y {pok2.nombre} queda inconsciente.")
                break
            else:
                print(f"{pok1.nombre} ataca, {pok2.nombre} ahora tiene {pok2.vida} hp de vida.")
                print("\n==Próxima RONDA===")
        else:
            pok1.vida = pok1.vida - pok2.ataque
            turno = 1
            if pok1.vida <= 0:
                print(f"{pok2.nombre} ataca y {pok1.nombre} queda inconsciente.")
                break
            else:
                print(f"{pok2.nombre} ataca, {pok1.nombre} ahora tiene {pok1.vida} hp de vida.")
                print("\n==Próxima RONDA===")
    #Consultamos que el pokemon 1 perdio
    if pok1.vida <= 0:
        Pokemon.gano(pok2)
    else:
        Pokemon.gano(pok1)
    print("-----0-----")
    cerrar = int(input("Escribe 1 para volver a jugar.\nEscribe 2 para cerrar.\n> "))
    if cerrar == 1:
        print("Reiniciando...")
        print("---0---")
    else:
        print("Cerrando...")
        print("---0---")
        break