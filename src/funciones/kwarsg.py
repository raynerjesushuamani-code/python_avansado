# crear una funcion que em permita saber de una lista de ingredientes cual es el de mayor precio
# ejemplo
# entrada: ajo=2 , papa=3 . aceite=8
# salida: el ingrediente de mayor precio es aceite
def ingrediente_caro(ingredientes):
    mayor_precio = 0
    ingrediente_caro = ""

    for ingrediente, precio in ingredientes.items():
        if precio > mayor_precio:
            mayor_precio = precio
            ingrediente_caro = ingrediente

    return ingrediente_caro, mayor_precio


# ingredientes con sus precios
ingredientes = {
    "Arroz": 4.50,
    "Pollo": 12.0,
    "Papa": 3.0,
    "Carne": 25.0,
    "Tomate": 5.50
}

resultado = ingrediente_caro(ingredientes)

print("Ingrediente más caro:", resultado[0])
print("Precio:", resultado[1]) 