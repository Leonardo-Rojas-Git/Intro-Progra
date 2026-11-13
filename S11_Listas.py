

<Nuevas .f> = sorted, len, max, min, remove, pop 
#Las cadenas también se pueden recorrer, pero son inmutables, las listas sí, y comienzan con índice 0

Slicing: " 3:5 " del orden 3 al 4, o sea despues del : es indice excluyente
( ej. )
print(meses[::-1]) # invertida 

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
