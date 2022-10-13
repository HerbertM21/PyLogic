def aplicar_descuento(price, discount):
    return price - price * discount / 100
    
def aplicar_IVA(price, percentage):
    return price + price * percentage / 100

def precio_cesta(basket, function):
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

if __name__ == "__main__":
    basket = {}
    for i in range(5):
        price = float(input(f'{i+1}. Introduce el precio: '))
        discount = float(input(f'{i+1}. Introduce el descuento: '))
        basket[price] = discount
    print(f"El precio de la compra tras aplicar los descuentos es: ${precio_cesta(basket, apply_discount)}")
    print(f"El precio de la compra tras aplicar el IVA es: ${precio_cesta(basket, apply_IVA)}")
