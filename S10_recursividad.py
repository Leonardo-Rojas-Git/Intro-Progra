definición: Es una función que se llama a sí misma para resolver una versión más pequeña del mismo problema. (pila de llamadas) como DFS
Partes:
Representación mental: Cómo copias
1) Caso base: El caso más pequeño, que se resuelve directo, sin volver a llamarse. Es lo que detiene la recursión.  2)Caso recursivo: Se llama a sí misma 
con un argumento más cercano al caso base, y usa ese resultado para armar el suyo.
Notas:
#Podría ser pasar de un diagrama recursivo al acódigo en sí
#¿Cómo convierto algo par? lo multiplico por dos, y por dos más uno si IMPAR
#¿Cómo resuelvo?: tabla, n recursivo, caso base y con el n - 1

(1) Suma de dígitos de un número
def suma_digitos(n):
    if n < 10:                              # un solo dígito: es su propia suma
        return n
    return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))

(2) invierte una cadena
def invertir(s):
    if len(s) == 0:                  # cadena vacía
        return ""
    return invertir(s[1:]) + s[0]    # el primer carácter pasa al final

print(invertir("hola"))

(3) Palindromo
def es_palindromo(s):
    if len(s) <= 1:                 # 0 o 1 letras: siempre es palíndromo
        return True
    if s[0] != s[-1]:               # la primera y la última son distintas: no lo es
        return False
    return es_palindromo(s[1:-1])   # revisa lo que queda en el centro

(4) Máx de un lista
def maximo(lista):
    if len(lista) == 1:          # un solo elemento: ese es el máximo
        return lista[0]
    m = maximo(lista[1:])        # máximo del resto
    if lista[0] > m:             # el primero contra el máximo del resto
        return lista[0]
    return m

(5) MCD
def mcd(a, b):
    if b == 0:              # mcd(a, 0) = a
        return a
    return mcd(b, a % b)    # mcd(a, b) = mcd(b, a % b)

(6) núm en binario, vonversor
def binario(n):
    if n < 2:                              # 0 o 1: ya es un dígito binario
        return str(n)
    return binario(n // 2) + str(n % 2)    # dígitos anteriores + último dígito
