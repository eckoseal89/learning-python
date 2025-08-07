import os, load_dictionary

path = os.path.dirname(os.path.abspath(__file__))
dic1 = path + "\\12dicts-6.0.2\\American\\2of12.txt"

wordlist = load_dictionary.load(dic1)

for word in wordlist:
    w2 = word[::-1]
    if word == w2:
        print(word)