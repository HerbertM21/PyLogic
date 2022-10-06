from Modulos.Utilidades import tirar_dado

class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100
    def ganar(self):
        print("======================================================")
        print(f">>> {self.nombre} ganó esta batalla!!!")
        print("- Suerte para próxima vez!! -")
        print("======================================================")

p1 = Pokemon("Pikachu", 15)
p2 = Pokemon("Charizard", 14)

p1.vida = 100
p2.vida = 100
turno = tirar_dado(2)
print(turno)

print("======================================================")
print("- HA INICIADO LA BATALLA -")
print(f">>> {p1.nombre} VS {p2.nombre}")
print("======================================================")
while p1.vida > 0 and p2.vida > 0:
    if turno == 1:
        p2.vida = p2.vida - p1.ataque
        turno = 2
        print(f"(+) {p1.nombre} está atacando, {p2.nombre} ahora tiene {p2.vida}")
    else: 
        p1.vida = p1.vida - p2.ataque
        turno = 1 
        print(f"(+) {p2.nombre} está atacando, {p1.nombre} ahora tiene {p1.vida}")
if p1.vida <= 0:
    p2.ganar()
else:
    p1.ganar()