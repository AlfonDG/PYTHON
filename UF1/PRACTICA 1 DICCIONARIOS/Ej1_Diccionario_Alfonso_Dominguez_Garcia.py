diccionarioFrase = {}

frase = str(input("Introduzca la frase que deseé: ")).lower()

separarFrase = frase.split()

palabraRepetir = 0

for letras in separarFrase:

    palabraRepetir = separarFrase.count(letras)

    diccionarioFrase[letras] = palabraRepetir

print(diccionarioFrase)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)