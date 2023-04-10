hora = int(input("Introduzca una hora: "))

#He contemplado que el 0 sea una hora. En este caso las 12 de la noche,no del mediodía. Por lo que contará el 0 como Bona Nit.
#El condicional IF empieza en -1 por lo que una hora jamás será negativa
if hora <= -1:
    print(f"Has introducido una hora nula,en este caso -> {hora:>2} es inferior o igual a -1. No es una hora acorde. Vuelva a intentarlo")

elif hora >= 6 and hora <= 12:
    print(f"Bon Dia, son les -> {hora:>2} hores")

elif hora >= 13 and hora <= 20:
    print(f"Bona Tarda, son les -> {hora:>2} hores")

elif hora >= 21 or hora <= 5:
    print(f"Bona Nit, son les -> {hora:>2} hores")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)