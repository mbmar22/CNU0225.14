import random
import time
import operator 

# Generar números aleatorios
print(("\nGeneración de intervalos").title())
def generar_intervalos(cantidad):
    elementos = [
        max(2, cantidad // 4), max(1, cantidad // 2), cantidad

    ]
    return sorted(set(elementos))

cantidad = int(input("¿Cuántos números? "))
intervalos = generar_intervalos(cantidad)

print(intervalos)


# Generar números
print(("\nGeneración de números").title())
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

elementos, tiempo = generar_numeros(cantidad)

print(f"Duración: {tiempo}")


# Sortear números con método de burbuja
print(("\nSorteo de números con método de burbuja").title())
def sortear_numeros(datos):
    inicio = time.perf_counter()

    n = len(datos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    fin = time.perf_counter()
    tiempo = fin - inicio

    return datos, tiempo

sorteados, tiempo = sortear_numeros(elementos)

print(sorteados)
print(f"Ordenamiento: {tiempo:.6f} segundos")


# Sortear números con método binario
print(("\nSorteo de números con método binario").title())
def busqueda_binaria(datos, objetivo):
    inicio_tiempo = time.perf_counter()

    inicio = 1 # En el ejemplo ponían 0 aquí
    fin = len(datos) # Y aquí le restaban uno al len. Funciona igual si le pongo 1 al inicio y le quito el menos 1 a len??? Al parecer sí 

    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(medio)
        valor_medio = datos[medio]
        print(valor_medio)

        if valor_medio == objetivo:
            print(valor_medio)
            return medio, tiempo
        elif valor_medio < objetivo:
            print(valor_medio, inicio)
            inicio = medio + 1
        else:
            print(valor_medio, fin)
            fin = medio - 1

    fin_tiempo = time.perf_counter()
    tiempo_final = fin_tiempo - inicio_tiempo 

    return None, tiempo

# Prueba
prueba = [43, 39, 99, 11, 87, 31, 63, 100, 27, 64, 37, 8]
prueba.sort()
print(prueba)
print(busqueda_binaria(prueba, 99))