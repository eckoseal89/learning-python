def enrango(y,z,x= int(input("Introduce un número entero: "))):
    while True:
        try:
            #x = int(input("Introduce un número entero: "))
            if x > y and x < z:
                print("El número es: ",x)
            else:
                print("Error: el valor no está dentro del rango permitido ({min}..{max})".format(min=y,max=z))
            break
        except ValueError:
            print("Error: entrada incorrecta")
    
enrango(-10,10)