# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
x = 1
while x <= 10:
    print(x)
    x += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
lista = [10, 20, 30, 40, 50]
for l in lista:
    print(l)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
x = 1
result = 0
while x <= 100:
    result += x
    x += 1
print(result)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
for c in "Python":
    print(c)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
x = 1

while True:
    if x % 7 == 0 and x % 50 == 0:
        print (f"El primer número divisible entre 7 y 50 es {x}")
        break
    else:
        x += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}
for k in diccionario:
    print(k)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
x = 1
while x <= 20:
    if x % 2 == 0:
        print(x)
        x += 1
    else:
        x += 1
        pass

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
n = 10
for x in range(10):
    print(n)
    n -= 1

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
lista = [30, 10, 30, 20, 30, 40]
cuenta = 0
for n in lista:
    if n == 30:
        cuenta += 1
print(cuenta)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
