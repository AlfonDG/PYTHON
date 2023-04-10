#En este caso establecemos una variable que diga que seguir sea True de esta caso no pararemos hasta que lo digamos, similar al break pero más elegante
seguir = True

#Ahora haremos un While que mientras no sea False no parará de pedir el día mes y año
while seguir == True:

    #Pedimos al usuario en formato INTEGER o Números del día, mes y año

    day = int(input("Escriba el día: "))

    month = int(input("Escriba el mes: "))

    year = int(input("Escriba el año: "))

    #Directamente hacemos que si el día es menor o igual a 0 o bien es superior a 31 NO le permita al usuario continuar y saldrá mensaje de error
    '''Ahora si establecemos que el mes sea inferior o igual a 0 o si bien supera los 12 meses pues también saltará el mismo mensaje d eerror
    y tendrá que volver a establecer los números de nuevo y por último si establece un año que sea inferior a 0 pues... No estará bien tendrá que volver a establecer otro valor 
    para el año.'''
    if day <= 0 or day > 31 or month <= 0 or month > 12 or year <= 0:

        print("No has escrito una fecha válida... Ya que tanto el día el mes y el año son inferiores a 0 por lo tanto no es una fecha válida")

        print("Vuelva a escribir una fecha que sea adecuada")

        print("")

        seguir = True

    #A partir de aquí están todos los condicionales que permiten pasar a STRING el número del mes establecido, ya que Python permite la opción de str() para pasar de INTEGER a STRING

    #Y realizaremos un condicional hasta 12 que permita saber el mes en el que está y poder mostrar el mes en STRING. Es tedioso hacerlo de esta forma pero no he encontrado otra forma mejor de hacerlo

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