# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.

unset = {1,2,3,4,5}
print(unset)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.
unset.add(6)
print(unset)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?
unset.add(5)
print(unset)

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in unset)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
unset.remove(4)
print(unset)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.
unset.clear()
print(len(unset))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.
unset = {"manzana", "naranja", "platano"}
lista = list(unset)
print(lista[0])

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.symmetric_difference(set2))

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
