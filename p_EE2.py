<Notas>: numero % 10 da el último dígito y numero // 10 lo quita
(1) Con retorno 
def es_perfecto(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    return suma == numero

n = 0
while n <= 0:
    n = int(input("Ingrese un número entero positivo: "))

if es_perfecto(n):
    print(n, "SÍ es un número perfecto")
else:
    print(n, "NO es un número perfecto")
    
(2) Almacen de digitos con str()
def mostrar_persistencia(numero):
    cadena = str(numero)
    pasos = 0
    while numero >= 10:
        producto = 1
        while numero > 0:
            producto = producto * (numero % 10)
            numero = numero // 10
        numero = producto
        cadena = cadena + " -> " + str(numero)
        pasos = pasos + 1
    print(cadena)
    if pasos == 1:
        print("Persistencia multiplicativa: 1 paso")
    else:
        print("Persistencia multiplicativa:", pasos, "pasos")
        
n = 0
while n <= 0:
    n = int(input("Ingrese un número entero mayor que 0: "))

mostrar_persistencia(n)
