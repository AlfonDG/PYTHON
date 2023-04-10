#Fem la creació del contador de Punt inicials a 0 i anirá sumant d'un punt en punt
contadorPuntos = 0

#Creació de les variables per a cada pregunta a fer
pregunta1 = str(input("1. La teva parella sembla estar més inquieta del normal sense cap motiu aparent."))

pregunta2 = str(input("2. Ha augmentat les despeses de vestuari."))

pregunta3 = str(input("3. Heu perdut l'interès que mostrava anteriorment per tu."))

pregunta4 = str(input("4. Ara s'afaita i es neteja amb més freqüència (si és home) o ara es arregla els cabells i es neteja amb més freqüència (si és dona)."))

pregunta5 = str(input("5. No us deixa que miris l'agenda del telèfon mòbil."))

pregunta6 = str(input("6. De vegades té trucades que diu no voler contestar quan ets tu davant."))

pregunta7 = str(input("7. Últimament es preocupa més a cuidar la línia i/o estar bronzejat/da."))

pregunta8 = str(input("8. Molts dies ve tard després de treballar perquè diu que té molt més feina."))

pregunta9 = str(input("9. Has notat que darrerament es perfuma més."))

pregunta10 = str(input("10. Es confon i et diu que ha estat a llocs on no ha anat amb tu."))

print("")

#Sequencia de condicionals que cada un comporvarà que hagi escrit Veritat o Fals segons i mostrarà el missatge corresponent.

if pregunta1 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta1:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")

elif pregunta1 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta1:>2} NO contarà punts")

print("----------------------")

if pregunta2 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta2:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta2 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta2:>2} NO contarà punts")


print("----------------------")

if pregunta3 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta3:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta3 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta3:>2} NO contarà punts")

print("----------------------")

if pregunta4 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta4:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta4 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta4:>2} NO contarà punts")

print("----------------------")

if pregunta5 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta5:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta5 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta5:>2} NO contarà punts")

print("----------------------")


if pregunta6 == "Veritat":

    print(f"Has contestat a aquesta pregunta -> {pregunta6:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de **** {contadorPuntos:^2} punts")


elif pregunta6 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta6:>2} NO contarà punts")

print("----------------------")

if pregunta7 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta7:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta7 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta7:>2} NO contarà punts")

print("----------------------")

if pregunta8 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta8:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta8 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta8:>2} NO contarà punts")

print("----------------------")

if pregunta9 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta9:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")


elif pregunta9 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta9:>2} NO contarà punts")

print("----------------------")

if pregunta10 == "Veritat":

    print(f"Has contestat a aquesta pregunta **** {pregunta10:>2} per lo que contará un punt")

    contadorPuntos += 3

    print(f"Portes un total de -> {contadorPuntos:^2} punts")

elif pregunta10 == "Fals":

    print(f"Has contestat a aquesta pregunta **** {pregunta10:>2} NO contarà punts")

print("----------------------\n")

#Segon apartat del enunciat: Saber si la nostra parella és infidel amb un total de 3 condicionals i amb el contador definitiu amb la seva respectiva puntuació

if contadorPuntos >= 0 or contadorPuntos <= 10:

    print(f"Has fet un total de ^^^^ {contadorPuntos:^2}\n")

    print("Enhorabona! la teva parella sembla ser totalment fidel.")

elif contadorPuntos <= 11 or contadorPuntos >= 22:

    print(f"Has fet un total de ^^^^ {contadorPuntos:^2}\n")

    print(" Potser hi ha el perill d'una altra persona a la seva vida o a la seva ment, encara que segurament serà una cosa sense importància. No baixis la guàrdia.")

elif contadorPuntos <= 22 or contadorPuntos >= 30:

    print(f"Has fet un total de ^^^^ {contadorPuntos:^2}\n")

    print(" La teva parella té tots els ingredients per estar vivint un romanç amb una altra persona. T'aconsellem que indaguis un poc més i esbrinis que és el que està passant pel seu cap")

else:
    print("No hem pogut realitzar la gestió de punts")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)