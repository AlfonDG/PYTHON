numUsuariosAnadir = int(input("Introduzca el número de veces que desea añadir usuarios: "))

def validador_noms_usuaris(numUsuariosAnadir):

    nombreUsuario = str(input("Introduzca el Nombre del usuario: "))

    if len(nombreUsuario) <= 6:

        print("")

        return f"El nombre establecido {nombreUsuario} de usuario ha de contener al menos 6 carácteres"

    elif len(nombreUsuario) >= 12:

        print("")

        return f"El nombre establecido {nombreUsuario} de usuario no puede contener más de 12 carácteres"

    elif not nombreUsuario.isalnum():

        print("")

        return f"El nombre establecido {nombreUsuario} de usuario solamente puede contener letras y números"

    else:
        print("")

        return True

while numUsuariosAnadir > 0:

    numUsuariosAnadir -= 1

    print(validador_noms_usuaris(numUsuariosAnadir))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)
print("")