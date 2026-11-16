import random

# Generar números aleatorios
def generar_intervalos(cantidad):
    elementos = [
        max(2, cantidad // 4), max(1, cantidad // 2), cantidad

    ]
    return sorted(set(elementos))

cantidad = int(input("¿Cuántos números? "))
intervalos = generar_intervalos(cantidad)

print(intervalos)


# Generar números
def generar_numeros(cantidad):
    datos = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    return datos

datos = generar_numeros(cantidad)
print(datos)