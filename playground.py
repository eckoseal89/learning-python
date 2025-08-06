"""Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string."""

def addnum(frase):
    if frase.isdigit():
        return str(frase + 1)
    if len(frase) > 1:
        if not frase[-1].isdigit():
            return frase+"1"
        else:
            x = -2
            while True:
                if frase[x].isdigit():
                    x -=1
                else:
                    x+=1
                    break
        num = int(frase[x:])
        num+=1
        l=len(frase[x:])
        frase = frase[:x] + str(num).zfill(l)
        return frase
    else:
        if len(frase) == 0:
            return 1        
        elif frase.isdigit():
            return str(int(frase)+1)
        else:
            return str(frase) + "1"

print(addnum("1"))
