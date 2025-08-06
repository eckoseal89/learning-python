text1 = input("Introduce el primer texto:")
text2 = input("Introduce el segundo texto:")

if sorted(list(text1.lower().replace(" ",""))) == sorted(list(text2.lower().replace(" ",""))):
    print("Los textos son anagramas")

else:
    print("Los textos NO son anagramas")
