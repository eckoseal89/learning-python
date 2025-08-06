""" 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.

2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.

4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].

5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] 
y almacÃ©nalo en una variable. Imprime la variable y la lista.

7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.

8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.

9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. 
Imprime la lista resultante.

10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van 
desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
"""

lista1 = [1,2,3,4,5]
print(lista1)

lista2 = [10, 20, 30, 40, 50]
print(lista2[2])

list3 = [1, 2, 3, 4, 5]
list3.append(6)
print(list3[-1])
print(list3)

list4 = [10, 20, 30, 40, 50]
list4.insert(1, 15)
print(list4)

lista5 = [10, 20, 30, 30, 40, 50]
lista5.remove(30)
print(lista5)

lista6 = [1, 2, 3, 4, 5]
pop = lista6.pop()
print(lista6, pop)

lista7 = [100, 200, 300, 400, 500]
lista7.sort(reverse=True)
print(lista7)

lista8 = [3, 1, 4, 2, 5]
lista8.sort()
print(lista8)

lista1, lista2 = [1,2,3], [4,5,6]
lista3 = lista1 + lista2
print(lista3)

lista = [10, 20, 30, 40, 50]
lista2 = lista1[0:2]
print(lista2)