def anagrama(a, b):
    if sorted(a) == sorted(b):
        print(f"{a} y {b} son anagramas")
    else:
        print(f"{a} y {b} no son anagramas")

a = str(input("a = "))
b = str(input("b = "))

anagrama(a, b)
