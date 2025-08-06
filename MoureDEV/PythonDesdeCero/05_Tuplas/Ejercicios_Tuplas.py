# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.
tupla = (10, 20, 30, 40, 50)
print(tupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.
tupla = (100, 200, 300, 400, 500)
print(tupla[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tupla = (1, 2, 3)
#tupla[0] = 10

# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
tupla = (1, 2, 3, 3, 4, 5, 3)
print(tupla.count(3))

# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
tupla = ("Java", "Python", "JavaScript", "Python")
print(tupla.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla = tupla1 + tupla2
print(tupla)

# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
tupla = (10, 20, 30, 40, 50)
subtupla = tupla[1:3]
print(subtupla)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tupla = ("rojo", "verde", "azul")
tupla = list(tupla)
tupla[1] = "amarillo"
tupla = tuple(tupla)
print(tupla)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1,2,3,4,5)
del my_tuple
#cprint(my_tuple)

# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tupla = (100, )
print(tupla)

