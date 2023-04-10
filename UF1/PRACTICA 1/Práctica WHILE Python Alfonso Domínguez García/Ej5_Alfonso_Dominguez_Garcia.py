
seguir = True

while seguir == True:

    day = int(input("Escriba el día: "))

    month = int(input("Escriba el mes: "))

    year = int(input("Escriba el año: "))

    if day <= 0 or day > 31 or month <= 0 or month > 12 or year <= 0:

        print("No has escrito una fecha válida... Ya que tanto el día el mes y el año son inferiores a 0 por lo tanto no es una fecha válida")

        print("Vuelva a escribir una fecha que sea adecuada")

        print("")

        seguir = True

    elif month == 1:

        month = str("Enero")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False

    elif month == 2:

        month = str("Febrero")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False

    elif month == 3:

        month = str("Marzo")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False

    elif month == 4:

        month = str("Abril")

        print("La fecha que has introducido será", day, "", month, "", year)

        seguir = False


    elif month == 5:

        month = str("Mayo")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 6:

        month = str("Junio")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 7:

        month = str("Julio")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 8:

        month = str("Agosto")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 9:

        month = str("Septiembre")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 10:

        month = str("Octubre")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False

    elif month == 11:

        month = str("Noviembre")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False


    elif month == 12:

        month = str("Diciembre")

        print("La fecha que has introducido será", day, "de", month, "de", year)

        seguir = False

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)