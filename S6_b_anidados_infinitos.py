La Matriz Ortogonal (Independencia): El bucle externo controla las filas (Y) y el interno las columnas (X). Sus rangos no se mezclan. (Ej. Procesar píxeles en una pantalla o días en una semana).
​El Límite Dinámico (Dependencia): El límite del range() del bucle interno es, matemáticamente, la variable iteradora del bucle externo. (Ej. Combinatoria, donde el segundo elemento siempre debe ser mayor al primero).
​El Reseteo de Estado (Acumulador Local vs Global): La trampa mortal de los anidados. Saber qué variables se inicializan en la línea 1 del programa (Globales) y qué variables se deben inicializar dentro del bucle externo, pero antes del interno (Locales).

1) 
for i in range(1,6):
    print(f"Alumno {i} ingresa tu nota: ")
    suma = 0
    for j in range(1,5):
        n_general = int(input(f"Nota {j}: "))
        suma = suma + n_general
    promedio = suma/4
    print(f"Promedio del alumno {i} es: {promedio:.2f}")
    print("="*20)
2) #Se hizo arreglos con 2 iteraciones
import random as rm
for i in range(1,6):
    for j in range(1,5):
        alea = rm.randint(1,5)
        print(alea, end="  ")
    print()
3) #Arreglos con i y j
n = int(input("Arreglo de n: "))
while( n %2 !=0):  #Primer filtro de dato correcto
    print("Error")
    n = int(input("N: "))
a = n/2             #Variable auxiliar que me da criterio

for i in range(1, n+1):    
    for j in range(1, n+1):
        if i <= a:  #Dentro de mi condición el i Significa que el criterio es por fila
            print("*", end=" ")
        else:
            print("o", end=" ")
    print()





< TIPS EE:>
