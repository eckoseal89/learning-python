dic1 = "C:\\Users\\david\\Nextcloud\\David\\learning-python\\Ejercicios\\ImpracticalPythonProjects\\FindingPalingram\\12dicts-6.0.2\\International\\3of6all.txt"
f = open(dic1, "r")

for w in f:
    w2 = w[::-1]
    if w == w2:
        print(w)