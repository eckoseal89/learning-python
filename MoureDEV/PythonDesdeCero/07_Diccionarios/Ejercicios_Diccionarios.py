# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
dic1 = {"name":"David", "age":35, "country":"ESP"}
print(dic1)

# 2. Accede al valor de la clave name en el diccionario.
print(dic1["name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
dic1["job"]="teleco"
print(dic1)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
dic1["age"] = 38
print(dic1)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del dic1["country"]
print(dic1)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
dic2 = {1:1,2:4,3:9,4:16,5:25}
print(dic2)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
dic1 = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in dic1)

# 8. Imprime solo las claves del diccionario.
print(dic1.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
listdic = list(dic1)
print(listdic)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
lista = ["name", "age", "job"]
dicnew = dict.fromkeys(lista, "Desconocido")
print(dicnew)