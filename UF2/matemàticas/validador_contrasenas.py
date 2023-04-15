numContrasenas = int(input("Introduzca el número de contraseñas que desea añadir: "))

def validador_contrasenas(numContrasenas):

    contrasena = input("\nIntroduzca la contraseña a continuación: ")

    if len(contrasena) < 8:

        print("")

        return f"La contraseña seleccionada {contrasena} es insegura. No contiene un mínimo de 8 carácteres. Escoga otra por favor"

    elif not contrasena.islower() and contrasena.isupper() and contrasena.isdigit() and contrasena.isalnum():

        print("")

        return f"La contraseña seleccionada {contrasena} es insegura. No contiene minúsuclas, mayúsuclas, números y al menos 1 carácter no alfanumerico como @. Escoga otra por favor"

    elif " " in contrasena:

        print("")

        return f"La contraseña seleccionada {contrasena} contiene espacios en blanco. No es segura, vuelva a escoger otra contraseña por favor"

    else:
        print("")

        return True

while numContrasenas > 0:

    numContrasenas -= 1

    print(validador_contrasenas(numContrasenas))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Ryan Haizour"

print(autor)
print(copy)
print("")