

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

(3) Cómo invertir el orden de los valores 
n = []
for i in range(4):
    n.append(int(input("Ingresa tus numeros: ")))
#Opción1:
print(n[::-1])
#Op2
for i in range(len(numeros) - 1, -1, -1): # Inicio "-1 pq si no, no inicia desde el último valor" , Fin "-1 el fin siempre es excluyente, o sea termina en [0], Paso "-1 pq retrocede".
    print(numeros[i])
(4) 
def promedio(lista):
    #cómo sumar sin sum()
    suma = 0
    for i in lista:
        suma = suma + i  #fin
    promedio = suma/len(lista)
    print(f"Este es el promedio: {promedio}")
    
    conta_1 = 0
    conta_2 = 0
    for i in lista:
        if i < promedio:
            conta_1 = conta_1 + 1
        elif i > promedio:
            conta_2 = conta_2 + 1
    print(f"Por debajo del promedio  hay: {conta_1}")
    print(f"Por encima del promedio hay: {conta_2}")

l = []
for i in range(4):
    l.append(int(input("Ingresa tus numeros: ")))
promedio(l) #le envio lista vacia para que lo rellene


(5)IMPORTANTE: Cómo eliminar duplicados
def eliminar_duplicados(lista): #NUNCA usar for y pop a la vez, se complica
    #### Opcion 1 ####
    i = 0
    # Recorremos cada elemento base
    while i < len(lista):
        j = i + 1  #(busca duplicados a la derecha de 'i')
        
        while j < len(lista):
            if lista[i] == lista[j]:
                # Encontramos un duplicado, lo eliminamos.
                lista.pop(j)
                # Al hacer pop, el elemento que estaba a la derecha se deslizó hacia la izquierda, 
                # ocupando exactamente el mismo índice 'j' que acabamos de vaciar.
            else:
                # Solo avanzamos si no hubo eliminación
                j += 1
                
        i += 1  # Avanzamos al siguiente elemento base

    print(f"Lista limpia: {lista}")
    
    #### Opcion 2 (modificando la lista) ###
    # Empezamos en el último índice válido, nos detenemos luego del índice 0, retrocediendoo -1
    for i in range(len(lista) - 1, -1, -1):
        
        # Si el elemento actual existe más de una vez en la lista global...
        if lista.count(lista[i]) > 1:
            # Lo eliminamos. Al ir en reversa, siempre eliminamos las copias redundantes
            # y dejamos viva la primera aparición original del número.
            lista.pop(i)
            
    print(f"Lista limpia: {lista}")
   
l = []
for i in range(6): # depende cuantos quieres
    l.append(int(input("Ingresa tus numeros: ")))
eliminar_duplicados(l)


(6) Buscar en lista de strings
def letras(lista, letra): 
    ### opción 1 ### modificando la lista:
    i = 0    
    while i < len(lista):
        # 1. Extraemos la primera letra (índice 0) 
        primera_letra = lista[i][0]
    
        if primera_letra != letra:
            lista.pop(i)
            # ALERTA: No sumamos 'i = i + 1' aquí. 
            # Al hacer pop, el siguiente nombre se deslizó a la posición actual 'i'.
            # En la siguiente vuelta, el bucle evaluará correctamente ese nuevo nombre.
        else:
            # Solo avanzamos si confirmamos que este nombre SÍ se queda.
            i = i + 1
    print(lista)
    
    ###opcion 2 ### PQ pide retornar
    nombres_filtrados = []
    # Volver la letra a minuscula para evitar errores 
    letra = letra.lower()
    
    # 2. Bucle de recorrido
    for nombre in lista:
        
            # nombre[0] extrae el primer carácter de la cadena de texto
            if nombre[0].lower() == letra:
                nombres_filtrados.append(nombre)
    # 3 Retorno de la nueva lista construida
    return nombres_filtrados
          
l = []
for i in range(4): # depende cuantos quieres
    l.append(input("Ingresa tus nombres: "))
word = input("Letra: ")
letras(l, word)


(7)
def eliminar_duplicados(lista):  #imaginando que ya de input lista
    # Inicializamos la estructura en blanco para la nueva lista
    lista_unicos = []
    
    # 2. Recorremos los datos de la lista original de principio a fin
    for elemento in lista:
        # 3. Filtro de pertenencia
        # Si el elemento actual AÚN NO existe dentro de nuestra nueva lista, lo insertamos.
        # Si ya existe (es un duplicado), el motor lo ignora y avanza al siguiente.
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
            
    # 4. Retorno obligatorio de la estructura procesada
    return lista_unicos
    
(10) NO. No es necesario recorrer la lista completa.  Lineal, binaria
def buscar_numero(numero_objetivo):
    # La lista ya viene escrita 
    lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] #[cite: 1]
    encontrado = False
    
    for elemento in lista_ordenada:
        if elemento == numero_objetivo:
            encontrado = True
            break
        elif elemento > numero_objetivo:
            break 
            
    if encontrado:
        print("Se encontró el número") #[cite: 1]
    else:
        print("No se encontró.") #[cite: 1]

# Solo pedimos el dato a buscar y llamamos a la función
num = int(input("Ingrese el número a buscar: "))
buscar_numero(num)
