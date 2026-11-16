## 1. Funciones Básicas Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo (números enteros o flotantes)
# y retorne su área calculada. Pruéballlamándola con dos valores distintos e imprime el resultado.
def calcular_area_rectangulo (b,h):
    return b*h
print(calcular_area_rectangulo(34,5))
print(calcular_area_rectangulo(4.5,6.7))
# ejrcicio 2    
def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    return precio * (1 + impuesto) * (1 - descuento)

precio = float(input("Ingrese el precio del producto: "))

resultado = calcular_precio_final(precio, descuento=0.05)

print("El precio final es:", resultado)
# ejrcicio  3
def obtener_promedio(numeros: list[int]) -> float:
    return sum(numeros) / len(numeros)

numeros = []

cantidad = int(input("¿Cuántos números desea ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("El promedio es:", obtener_promedio(numeros))
# ejercicio 4
def unir_frases(*args: str) -> str:
    return " ".join(args)

cantidad = int(input("¿Cuántas frases desea ingresar?: "))

frases = []

for i in range(cantidad):
    frase = input(f"Ingrese la frase {i+1}: ")
    frases.append(frase)

print("Oración final:", unir_frases(*frases))
#ejercio 5
def generar_perfil_usuario(**kwargs) -> str:
    perfil = ""

    for clave, valor in kwargs.items():
        perfil += f"{clave}: {valor}\n"

    return perfil

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país: ")
profesion = input("Ingrese su profesión: ")

print(generar_perfil_usuario(
    nombre=nombre,
    edad=edad,
    pais=pais,
    profesion=profesion
))
# ejercicio 6
es_par = lambda numero: numero % 2 == 0

numero = int(input("Ingrese un número: "))

print(es_par(numero))
# ejercico 7
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.

    Parámetros:
        base (float): Número base.
        exponente (float): Exponente no negativo.

    Restricciones:
        El exponente no debe ser negativo.

    Retorna:
        float: Resultado de la potencia.
    """
    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo")

    return float(base ** exponente)


base = float(input("Ingrese la base: "))
exponente = float(input("Ingrese el exponente: "))

print("Resultado:", calcular_potencia(base, exponente))
#ejercico 8
def crear_validador_limite(limite_maximo: int):

    def validar(numero):
        return numero <= limite_maximo

    return validar


limite = int(input("Ingrese el límite máximo: "))

validador = crear_validador_limite(limite)

numero = int(input("Ingrese un número para validar: "))

print(validador(numero))
#ejercicio 9
precios: list[float] = []

cantidad = int(input("¿Cuántos precios ingresará?: "))

for i in range(cantidad):
    precio = float(input(f"Ingrese el precio {i+1}: "))
    precios.append(precio)

precios_actualizados = list(map(lambda precio: precio * 1.10, precios))

print("Precios actualizados:", precios_actualizados)
#ejercicico 10
palabras: list[str] = []

cantidad = int(input("¿Cuántas palabras ingresará?: "))

for i in range(cantidad):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

palabras_filtradas = list(filter(lambda palabra: len(palabra) > 4, palabras))

print("Palabras con más de 4 caracteres:", palabras_filtradas)


