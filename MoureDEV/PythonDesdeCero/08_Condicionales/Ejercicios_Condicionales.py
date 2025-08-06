# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.

def tiponumero(num):
    if num > 0:
        print("El número es positivo")
    elif num == 0:
        print("El número es 0")
    else:
        print("El número es negativo")

num=int(input("Intoruduce un número: "))
tiponumero(num)

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
edad = int(input("Intoruduce tu edad: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
cadena="hola"

if len(cadena) == 0:
    print("La cadena de texto está vacia")
else:
    print(f"La cadena de texto es '{cadena}'")


# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num1 == num2:
    print("Los números son iguales")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
num1 = 15

if num1 % 5 == 0 and num1 % 3 == 0:
    print("El número es divisible entre 3 y 5")
else:
    print("El número no es divisible entre 3 y 5")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
num1 = int(input("Introduce un número: "))

if num1%2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.


# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).

# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.