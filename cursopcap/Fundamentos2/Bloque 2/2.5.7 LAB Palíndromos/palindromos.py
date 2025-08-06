valid=0
while valid==0:
    text = input("Introduce a continuación el texto a comprobar:")
    text=text.upper().replace(" ","")
    #rtext=text[::-1]

    if len(text) > 0:

        if text == text[::-1]:
            print("El texto introducido es un palíndromo")

        else:
            print("El texto introducido NO es un palíndromo")
        valid=1
    else:
        print("No has introducido un texto válido")
