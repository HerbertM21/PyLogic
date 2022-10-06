# VALIDACIÓN DE NOMBRE
N_Permitidos = ["Herbert Mayorga","Juan Lopez","Lucas Perez"]
dueño = "Herbert Mayorga"

print("============================================================")
print(                   "INGRESO DE USUARIO"                       )
print("============================================================")
nombre = str(input("+ Ingrese su nombre completo para validación: ")).title()

while not nombre in N_Permitidos: 
	print("Usted no pertenece a la organización.")	
	print("============================================================")
	nombre = input("Ingrese su nombre completo para validación: ").title()
print("============================================================")
print("--- Bienvenido "+nombre+", has entrado al panel administrativo ---")
print("============================================================")

while nombre == dueño:
	print("Otorgando permisos individuales...")
	break

print("============================================================")
num = (input("Ingrese un número: "))
while not num.isdigit():
	print("Incorrecto. Ingrese nuevamente.")
	num = (input("Ingrese un número: "))
print("---- Número "+num+"----")
