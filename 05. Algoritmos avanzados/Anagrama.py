def check_anagram(a, b):
    if a is None or b is None or len(a) != len(b):
        return "No es anagrama"
        
    contador_a = {}
    contador_b = {}
    
    for i in a:
        if i not in contador_a.keys():
            contador_a[i] = 1
        else:
            contador_a[i] += 1
        
    for i in b:
        if i not in contador_b.keys():
            contador_b[i] = 1
        else:
            contador_b[i] += 1
    print(contador_a)
    print(contador_b)
    return "Es anagrama" if contador_a == contador_b else "No es anagrama"

print(check_anagram("mora", "roma"))
#{'m': 1, 'o': 1, 'r': 1, 'a': 1}
#{'r': 1, 'o': 1, 'm': 1, 'a': 1}