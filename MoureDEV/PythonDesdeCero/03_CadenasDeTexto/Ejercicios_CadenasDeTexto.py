# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

text = "Aprendiendo Python"
print(len(text))

a , b = "Hola", "Python"
c = a + b
print(c)

print("Hola\nPython")

nombre, apellido, edad = "David", "Tena", 35
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

a, b, c, d, e, f = "Python"
print(f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}")

pal = "Programación"
print(pal[3:8])

p = "Python"
print(p[::-1])

frase = "aprendiendo python"
print(frase.upper())

print(pal.count("n"))

num = "12345"
print(num.isdigit())