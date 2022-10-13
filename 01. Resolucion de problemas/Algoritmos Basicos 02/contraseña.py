import random as r
import string as s

def generador_contrasena():
    caracteres = s.ascii_letters + s.digits
    contrasena = ""
    for i in range(15):
        contrasena += r.choice(caracteres)
    return contrasena

def contrasenas(numero: int) -> int:
    print('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
    for i in range(numero):
        print(f"{i+1}.- NEW PASSWORD: {generador_contrasena()}")
    print('''
██╗░░██╗███████╗██████╗░██████╗░███████╗██████╗░████████╗░░░  ███╗░░░███╗  ░░██╗██████╗░
██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝░░░  ████╗░████║  ░██╔╝╚════██╗
███████║█████╗░░██████╔╝██████╦╝█████╗░░██████╔╝░░░██║░░░░░░  ██╔████╔██║  ██╔╝░░█████╔╝
██╔══██║██╔══╝░░██╔══██╗██╔══██╗██╔══╝░░██╔══██╗░░░██║░░░░░░  ██║╚██╔╝██║  ╚██╗░░╚═══██╗
██║░░██║███████╗██║░░██║██████╦╝███████╗██║░░██║░░░██║░░░██╗  ██║░╚═╝░██║  ░╚██╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝  ╚═╝░░░░░╚═╝  ░░╚═╝╚═════╝░''')

if __name__ == "__main__":
    numero = int(input("Ingrese el número de contraseñas que desea: "))
    contrasenas(numero)