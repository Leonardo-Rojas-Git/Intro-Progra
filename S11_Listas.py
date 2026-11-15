

<Nuevas .f> = sorted, len, max, min, remove, pop 
# " el_eliminado = lista.pop(0) " saca el elemento en el índice 0 y se almacena en tu variable
#" nueva_lista = lista.remove(35) " elimina la primera aparicion del valor 35, y la variable queda con la nueva lista.
#Las cadenas también se pueden recorrer, pero son inmutables, las listas sí, y comienzan con índice 0

Slicing: " 3:5 " del orden 3 al 4, o sea despues del : es indice excluyente
( ej. )
print(meses[::-1]) # [Inicio, fin, paso]. paso: Cuántos elementros saltar y en que sentido

(1)
import random as rm
Lis = []
for i in range(10):
    Lis.append(rm.randint(10,99))
print(Lis)
#Función qu elimina pares 
a = 0
while a < len(Lis):
    if Lis[a] % 2 == 0:
        
        Lis.pop(a)
    else:
        a = a + 1
print(Lis)
(Valor): elminar pares de una lista con while


(2) Cómo encontrar el máximo valor de una lista sin max()
lista = [15, 19, 1, 20, 2 ]
# se asumuría que el primero es el mayor
mayor_valor = lista[0]
for elemento in lista:
    # elemento primero es 15, luego, 19... hasta ser 2
    if elemento > mayor_valor:  
        #si no se cumple entonces el mayor no se actualiza
        mayor_valor = elemento
