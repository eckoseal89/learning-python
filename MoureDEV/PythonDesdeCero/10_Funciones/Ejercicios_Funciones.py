# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(nombre = "desconocido"):
    print(f"Hola, {nombre}")

personalized_greeting()

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.
def multiply(a, b):
    return(a * b)
result = multiply(2,3)
print(result)

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(444))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(texto):
    return texto.upper()
print(convert_to_uppercase("kcrneinEWDCvenor9"))

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*nums):
    suma = 0
    for num in nums:
        suma += num
    return suma
print(arbitrary_sum(2,5,786,3,2,654))

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(nombre = "John", apellido = "Doe"):
    return f"Hola, {nombre} {apellido}"

print(generate_full_greeting(apellido="Tena", nombre= "David"))

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponente):
    return base ** exponente
print(power(5,3))

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.
def calculate_average(num1, num2, num3):
    return (num1+num2+num3)/3
print(calculate_average(13,14,15))

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.
def count_characters(texto):
    return len(texto)

print(count_characters("lkncenruiunbc9843rv4reobnv fih348cnr4"))

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*textos):
    for texto in textos:
        print(texto.upper())
display_messages("hola", "adios", "otro Texto", "que tal")