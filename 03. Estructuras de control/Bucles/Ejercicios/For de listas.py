lista = ["Python", "Hola", "Pedro", "Youtube"]
for cadena in lista:
    print("---- "+cadena+" ----")
    for caracter in cadena:
        mini=caracter.lower()
        if mini in "aeo":
                print(mini)