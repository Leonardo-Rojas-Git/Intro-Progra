#Ojo con 
reporte_mejor_mes: la mayor calificación y el o los meses donde se obtuvo
obtener_columna(matriz, j) : lista con toda las calificaciones en algún mes
ordenar_descendente(ids, promedios) : listas paralelas se mueven juntas 

import random
# ==============================================================
# BLOQUE 1 · ENTRADA Y MATRIZ (E1–E3)
# ==============================================================

# E1 · Puntos 1, 6, 7 y 9: pide un entero hasta que esté entre minimo y maximo
def leer_entero(mensaje, minimo, maximo):
    valor = int(input(mensaje))
    while valor < minimo or valor > maximo:
        print("Error: ingresa un número entre", minimo, "y", maximo)
        valor = int(input(mensaje))
    return valor


# E2 · Punto 3: matriz de n videojuegos (filas) x m meses (columnas),
#      con calificaciones al azar de 0 a 10
def generar_matriz(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.randint(0, 10))
        matriz.append(fila)
    return matriz


# E3 · Punto 3: muestra la matriz en formato tabla
def mostrar_matriz(matriz):
    print("Juego", end="    ")
    for j in range(1, len(matriz[0]) + 1):
        if j < 10:
            print("Mes " + str(j), end="   ")
        else:
            print("Mes " + str(j), end="  ")
    print()   
    for i in range(1, len(matriz) + 1):
        if i < 10:
            print("VJ " + str(i), end="     ")
        elif i < 100:
            print("VJ " + str(i), end="    ")
        else:
            print("VJ " + str(i), end="   ")
            
        for valor in matriz[i - 1]:
            print(valor, end="       ")
        print()

# ==============================================================
# BLOQUE 2 · HERRAMIENTAS SIN MAX/MIN (E4–E7)
# ==============================================================

# E4 · Punto 4: promedio de cada videojuego (suma de sus meses / total de meses)
def calcular_promedios(matriz):
    promedios = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma = suma + matriz[i][j]
        promedios.append(suma / len(matriz[i]))
    return promedios


# E5 · Punto 4: todas las posiciones donde está el valor más alto (con empates)
def posiciones_del_mayor(lista): #argm: la lista promedios
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == mayor:
            posiciones.append(i)
    return posiciones


# E6 · Punto 4: todas las posiciones donde está el valor más bajo (con empates)
def posiciones_del_menor(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == menor:
            posiciones.append(i)
    return posiciones


# E7 · Punto 4: calificaciones de todos los videojuegos en el mes j
def obtener_columna(matriz, j): 
    columna = []
    for i in range(len(matriz)): #itera pasando de fila en fila dded videojuego, pero
        columna.append(matriz[i][j])# con un j col fijo
    return columna


# ==============================================================
# BLOQUE 3 · REPORTES DEL PUNTO 4 (E8–E10)
# ==============================================================

# E8 · Videojuego TOP: el o los videojuegos con el promedio más alto
def reporte_top(matriz):
    promedios = calcular_promedios(matriz) #ej. 7.3333
    posiciones = posiciones_del_mayor(promedios) #ok ese es el VJ 5
    print("Promedio más alto:", round(promedios[posiciones[0]], 2)) #pq solo hay 1 mayor promedio
    for k in range(len(posiciones)): #,pero lo pueden tener diferentes VJ
        print("Videojuego", posiciones[k]+1)  #importante no recorrer desde 1


# E9 · Videojuego menos calificado en CADA mes
def reporte_menor_por_mes(matriz):
    for j in range(len(matriz[0])): # tamaño de fila 1(lista) = num de meses
        columna = obtener_columna(matriz, j) # si j=0, col es una lista con los valores del mes 1
        posiciones = posiciones_del_menor(columna) # le saca el índice del menor valor = num de videojuego
        print("Mes", j + 1, "- calificación", columna[posiciones[0]], "- videojuego(s):", end=" ")
        for k in range(len(posiciones)): #Como en algún mes j (iteración) VA posiciones(lista) almacena un único valor
            print(posiciones[k] + 1, end=" ")#el índice del la menor nota, entonces [0]
        print() # por si hay EMPATE en la lista Posiciones habria otros indices (el # de videojuego) con esa nota
# o sea imprime el valor de ese índice (ej. VJ: 1, 3, 4)
# E10 · Mejor mes de CADA videojuego
def reporte_mejor_mes(matriz):
    for i in range(len(matriz)): #lo mismo que arriba, i: índice de filas (VJ i)
        posiciones = posiciones_del_mayor(matriz[i]) #recibe la una lista [] que contiene los valores del del (VJ i)
        print("Videojuego", i + 1, "- calificación", matriz[i][posiciones[0]], "- mes(es):", end=" ")# pq Posiciones es una lista que tiene todos los indices(meses) de aquellos que valores max del VJ
        for k in range(len(posiciones)):# pq puede haber EMPATE
            print(posiciones[k] + 1, end=" ") #Puede haber varios meses que cumplan ser valor máx
        print() #entonces imprimo tantas veces como elementos haya en la lista Posiciones

# ==============================================================
# BLOQUE 4 · RANKING, BÚSQUEDA Y AUMENTO (E11–E13)
# ==============================================================

# E11a · Punto 5: burbuja de mayor a menor; ids se intercambia junto con promedios
def ordenar_descendente(ids, promedios): #Ids: lista con los num de los VJs (primero estan en orden) al hacer en decreciente, ambos se tienen que desordenar de la misma manera
    n = len(promedios) #total de VJs
#¿Por qué basta con 1 pasada? Porque en una lista de 2 elementos, con mover el mayor al principio en una sola pasada, el otro elemento queda automáticamente acomodado en su lugar. No necesitas hacer más pasadas.
    for i in range(n - 1): #OJO
        for j in range(n - 1 - i):
#¿Qué pasa al final de esta primera pasada? El elemento más pequeño de todos (porque estamos ordenando de mayor a menor) se va indefectiblemente al último lugar de la lista. Ya está en su posición definitiva.
#Ya no compara con el más chikito pq está fijo al último
            if promedios[j] < promedios[j + 1]: #ej1
                aux = promedios[j] # entonces en lapocicion del pequeño va el grande
                promedios[j] = promedios[j + 1] #y en la posicion del grande va el pequeño
                promedios[j + 1] = aux
                aux = ids[j] # para no perder orden lo mismo con los ids
                ids[j] = ids[j + 1]
                ids[j + 1] = aux
#ej2
#if promedios[j] < promedios[j + 1]:
# Intercambiar promedios en una sola línea
#    promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
# Intercambiar ids de forma paralela
#    ids[j], ids[j + 1] = ids[j + 1], ids[j]


# E11b · Punto 5: ranking de videojuegos por promedio
def reporte_ranking(matriz):
    promedios = calcular_promedios(matriz)
    ids = [] 
    for i in range(len(matriz)):
        ids.append(i + 1)  #pq comienza en VJ 1 hasta el último VJ
    ordenar_descendente(ids, promedios)
    for k in range(len(ids)): #lista con el num de los VJs en el mismo orden que la lista promedios, 
        print("Puesto", k + 1, "- Videojuego", ids[k], "- promedio", round(promedios[k], 2))


# E12a · Punto 6: búsqueda lineal; primera posición de valor, o -1 si no está
def busqueda_lineal(lista, valor):#lista: alguna fila de la Matriz
    for i in range(len(lista)): # i: indice de lista 
        if lista[i] == valor:
            return i
    return -1 #poner en informe es el output de mensaje: no hay este valor en tu lista


# E12b · Punto 6: primer mes con 10 del videojuego que elija el usuario
def opcion_buscar_10(matriz):
    vj = leer_entero("Número de videojuego: ", 1, len(matriz)) #num VJ, minimo 1, max num de VJ
    pos = busqueda_lineal(matriz[vj - 1], 10) # le digo el valor de que índice quiero, y que valor quiero buscar linealmente
    if pos == -1:
        print("El videojuego", vj, "no obtuvo 10 en ningún mes")
    else:
        print("El videojuego", vj, "obtuvo su primer 10 en el mes", pos + 1)


# E13a · Punto 7: suma 1 a cada mes del videojuego i, sin pasar de 10
def aumentar_calificacion(matriz, i): #el num VJ le llega como indice
    for j in range(len(matriz[i])): #j: num col ( num del mese)
        if matriz[i][j] < 10: #solo si algun valor de toda la matriz es menor a 10 puedes sumar 1
            matriz[i][j] = matriz[i][j] + 1


# E13b · Punto 7: pide el videojuego y aplica el aumento (el cambio queda en la matriz)
def opcion_aumentar(matriz):
    vj = leer_entero("Número de videojuego: ", 1, len(matriz))
    aumentar_calificacion(matriz, vj - 1)
    print("Videojuego", vj, "- nuevas calificaciones:", matriz[vj - 1])


# ==============================================================
# BLOQUE 5 · RECURSIÓN Y MENÚ (E14–E15)
# ==============================================================

# E14a · Punto 8: cuenta los meses exitosos (7 o más) desde el mes j hasta el final
#   Caso base: j == len(fila), ya no quedan meses -> 0
#   Caso recursivo: lo que aporta el mes j + lo que cuentan los meses siguientes
def contar_exitosos(fila, j):
    if j == len(fila):
        return 0
    if fila[j] >= 7:
        return 1 + contar_exitosos(fila, j + 1)
    else:
        return contar_exitosos(fila, j + 1)


# E14b · Punto 8: meses exitosos del videojuego que elija el usuario
def opcion_exitosos(matriz):
    vj = leer_entero("Número de videojuego: ", 1, len(matriz))
    total = contar_exitosos(matriz[vj - 1], 0)
    print("El videojuego", vj, "tuvo", total, "de", len(matriz[vj - 1]), "meses exitosos (7 o más)")


# E15 · Punto 9: opciones del menú
def mostrar_menu():
    print()
    print("===== MENÚ =====")
    print("1. Mostrar matriz")
    print("2. Videojuego TOP")
    print("3. Videojuego menos calificado por mes")
    print("4. Mejor mes por videojuego")
    print("5. Ranking de videojuegos")
    print("6. Buscar el primer 10 de un videojuego")
    print("7. Aumentar calificación de un videojuego")
    print("8. Meses exitosos de un videojuego")
    print("9. Salir")


# ==============================================================
# PROGRAMA PRINCIPAL (E16)
# ==============================================================

# E16 · Puntos 1, 3 y 9: pide las cantidades, genera y muestra la matriz,
#       y atiende el menú hasta que se elija salir
def main():
    n = leer_entero("¿Cuántos videojuegos? (1-100): ", 1, 100)
    m = leer_entero("¿Cuántos meses? (1-20): ", 1, 20)
    matriz = generar_matriz(n, m)
    mostrar_matriz(matriz)
    opcion = 0
    while opcion != 9:
        mostrar_menu()
        opcion = leer_entero("Elige una opción: ", 1, 9)
        if opcion == 1:
            mostrar_matriz(matriz)
        elif opcion == 2:
            reporte_top(matriz)
        elif opcion == 3:
            reporte_menor_por_mes(matriz)
        elif opcion == 4:
            reporte_mejor_mes(matriz)
        elif opcion == 5:
            reporte_ranking(matriz)
        elif opcion == 6:
            opcion_buscar_10(matriz)
        elif opcion == 7:
            opcion_aumentar(matriz)
        elif opcion == 8:
            opcion_exitosos(matriz)
    print("Fin del programa")


main()
