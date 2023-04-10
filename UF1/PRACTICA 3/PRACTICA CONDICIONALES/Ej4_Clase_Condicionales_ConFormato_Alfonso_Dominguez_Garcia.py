dia = int(input("Escriba el día y le diré su horóscopo: "))

mes = str(input("Escriba el mes y le diré su horóscopo: "))

if dia >= 21 and mes == "Marzo" or dia <= 19 and mes == "Abril":
    print("Tu horóscopo es ARIES")

elif dia >= 20 and mes == "Abril" or dia <= 20 and mes == "Mayo":
    print("Tu horóscopo es TAURO")

elif dia >= 21 and mes == "Mayo" or dia <= 20 and mes == "Junio":
    print("Tu horóscopo es GÉMINIS")

elif dia >= 21 and mes == "Junio" or dia <= 22 and mes == "Julio":
    print("Tu horóscopo es CÁNCER")

elif dia >= 23 and mes == "Julio" or dia <= 22 and mes == "Agosto":
    print("Tu horóscopo es LEO")

elif dia >= 23 and mes == "Agosto" or dia <= 22 and mes == "Septiembre":
    print("Tu horóscopo es VIRGO")

elif dia >= 23 and mes == "Septiembre" or dia <= 22 and mes == "Octubre":
    print("Tu horóscopo es LIBRA")

elif dia >= 23 and mes == "Octubre" or dia <= 21 and mes == "Noviembre":
    print("Tu horóscopo es ESCORPIO")

elif dia >= 22 and mes == "Noviembre" or dia <= 21 and mes == "Diciembre":
    print("Tu horóscopo es SAGITARIO")

elif dia >= 22 and mes == "Diciembre" or dia <= 19 and mes == "Enero":
    print("Tu horóscopo es CAPRICORNIO")

elif dia >= 20 and mes == "Enero" or dia <= 18 and mes == "Febrero":
    print("Tu horósocopo es ACUARIO")

elif dia >= 19 and mes == "Febrero" or dia <= 20 and mes == "Marzo":
    print(f"Tu horóscopo es PISCIS")

else:
    print("No has escrito un día o mes adecuado. No sabemos tu horóscopo. Vuelva a intentarlo")

'''URL Web sobre los horóscopos -> 
https://www.cosmopolitan.com/es/horoscopo/extra/a36416643/horoscopo-signos-del-zodiaco-fechas/'''

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)