
def llegeix1a10():

    num1 = int(input("Introduzca un valor de 1 al 10: "))

    while num1 > 10 or num1 < 1:
        if num1 > 11 or num1 <= 0:
            return f"Error, el número {num1} no está fuera del rango"
        num1 = int(input("Introduzca un valor de 1 al 10: "))

    return f"El número se encuentra dentro del rango {num1}"

print(llegeix1a10())
