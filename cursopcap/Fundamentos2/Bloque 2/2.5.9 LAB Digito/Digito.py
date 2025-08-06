integ=False
while integ == False:
    nacim = input("Por favor introduce tu fecha de nacimiento (formato AAAAMMDD o AAAADMM o MMDDAAAA): ")
    if nacim.isdigit() and len(nacim) == 8:
        integ =True
    else:
        print("Debes introducir un formato numérico de fecha válido(formato AAAAMMDD o AAAADMM o MMDDAAAA)")

x=0
while len(nacim) > 1:
    for n in nacim:
        x+=int(n)
    nacim=str(x)
    x=0

print("Tu dígito de la vida es: ",int(nacim))
