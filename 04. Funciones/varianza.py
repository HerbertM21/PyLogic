def cuadrados(datos):
    list = []
    for dato in datos:
        list.append(dato**2)
    return list

def estadisticas(datos):
    stat = {}
    stat['media'] = round(sum(datos)/len(datos), 2)
    stat['varianza'] = round(sum(cuadrados(datos))/len(datos)-stat['media']**2, 2)
    stat['desviacion tipica'] = round(stat['varianza']**0.5, 2)
    return stat

if __name__ == "__main__":
    datos = []
    for i in range(5):
        datos.append(float(input('Introduce un dato: ')))
print(estadisticas(datos))
