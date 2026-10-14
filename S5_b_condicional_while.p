​El Centinela : solo si el resultado de la condición es F entonces: sale del bucle. si pones and, basta un F para que todo sea F.
​Aplicación en busqueda binaria
#Nuevo continue: como el break pero no de bota, sino que se teletrasporta al inicio del bucle sin leer lo demás


#Nuevo: PARÁMETRO para el print ** end= ** " 
for i in range(40, 61, 2):
    print(i, end=" ") 

#Nuevo: LIBRERÍA ** random ** para un número aleatorio
#Nuevo: ESTILO del print ** n\ ** corre una linea
import random as rdm
num = int(input("Ingresa tu número: "))
suma = 0
for i in range(1, num+1):
    aleatorio = rdm.randint(10, 99) #solo usar i para mostrar no en interar
    print(aleatorio, end=" ")
    suma += aleatorio
print(f"\nLa suma es {suma}") # O # print("\n" f"La suma es {suma}")

CASO: Almacenar nombres y acumulador
bandera = True
cantidad_nombres = 0
historial_nombres = ""  # name descriptivo

while bandera:
    caja = input("Ingresa un nombre (o 'fin' para terminar): ")
    
    # 1. El cortafuegos de salida
    if caja == "fin":
        bandera = False
    else:
        # 2. Acumuladores protegidos: Solo operan si la entrada no fue "fin"
        cantidad_nombres += 1
        historial_nombres = historial_nombres + " " + caja

# 3. Capa de presentación unificada (fuera del bucle)
print(f"Cantidad total de nombres ingresados: {cantidad_nombres}")
print(f"Nombres guardados: {historial_nombres}")

# ¿Cómo invertir un número contar sus digitos y sumarlos?
Molde lógico:
1)
invertido = 0
n_1 = n  # Guarda el valor original por si se necesita posteriormente
contador = 0
acumulador = 0

while True:
    a = n % 10
    acumulador += a
    invertido = invertido * 10 + a
    n = n // 10
    contador += 1
------------------------------------------------------------------------
1.1) #Detertor de primos y los muestra
n = int(input("Ingresa un número: "))
lista_primos = ""
while n >= 2:
    cantidad_divisores = 1 # el n es divisor de SI MISMO
    divisor = n
#fin validación input
    while True:
        divisor = divisor - 1
        if divisor == 0:
            break

        elif n % divisor == 0:
            cantidad_divisores = cantidad_divisores + 1
    #Vuelve al segundo while, solo acaba si: divisor == 0 
    if cantidad_divisores == 2:
        lista_primos += f" {n}" #automaticamente se convierte a cadena

    n = n - 1 #Como no uso el n ingresado, lo modifico, sino lo igualo a si mismo y me reservo el original

print("Primos encontrados:", lista_primos)
1.2) #cuantos primos hay desde 2 hasta un n de input
import math as mth
while True:
    n = int(input("Ingresa N: "))
    if n > 2:
        break
    print("N debe ser mayor que 2")

contador = 0
candidato_a_primo = 2      # candidato: avanza de 2 a N-1
while candidato_a_primo < n:
    posible_divisor = 2    # divisor: se reinicia en cada candidato
    while posible_divisor <= mth.sqrt(candidato_a_primo): # verificación dinámica
        if candidato_a_primo % posible_divisor == 0:
            break  # se validó que el número de prueba es divisor → no es primo
        posible_divisor += 1
    else:  #(else despues de while) solo se activa si no finalizó por BREAK → primo
        print(candidato_a_primo , end=" ") # candidato validad
        contador += 1
    candidato_a_primo += 1

print(f"\n{contador} primos")
5) Multifiguras
n = int(input("n: "))
espacios = n - 1                     # 1. primera fila
asteriscos = 1
for fila in range(n):
    for j in range(espacios):
        print(" ", end="")
    for j in range(asteriscos):
        if j == 0 or j == asteriscos - 1 or fila == n - 1:   # 3. qué va en cada posición
            print("*", end="")
        else:
            print(" ", end="")
    print()
    espacios -= 1                    # 2. cambio por fila
    asteriscos += 2

