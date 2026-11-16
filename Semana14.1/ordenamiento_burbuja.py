import random
import time
import operator 

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
    inicio = time.perf_counter()
    datos = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

elementos, tiempo = generar_numeros(cantidad)

datos = generar_numeros(cantidad)
print(f"Duración: {tiempo}")


# Sortear números
def sortear_numeros(datos, key):
    inicio = time.perf_counter()
    sorteados = sorted(datos, key = operator.itemgetter(key))
    fin = time.perf_counter()
    tiempo = fin - inicio
    return sorteados, tiempo

sorteados = sortear_numeros(datos, key)
print(f"Duración: {tiempo}")