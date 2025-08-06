filas=[]
columnas=[]
cuadras=[]

for n in range(9):
    filas.append(input("Introduce la fila "+str(n+1)+":"))

colu=""
for n in range(9):
    for f in filas:
        colu+=f[n]
    columnas.append(colu)
    colu=""

cuad=""
i=0
x=0
for n in range(9):
    for f in filas[x:x+3]:
        cuad+=f[i:i+3]
    cuadras.append(cuad)
    cuad=""
    if i==6:
        i=0
        x+=3
    else:
        i+=3
    
sudoku=[filas,columnas,cuadras]

for s in sudoku:
    for x in s:
        for n in range(9):
            if str(n+1) not in x:
                print("No")
                exit()
print("Yes")
        