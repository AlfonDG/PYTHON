valMin = int(input("Introduzca el valor mínimo: "))

valMax = int(input("Introduzca el valor máximo: "))

while valMin > valMax:
    valMin = int(input("Introduzca el valor mínimo: "))

    valMax = int(input("Introduzca el valor máximo: "))

def lecturaInterval(min,max):

    num = int(input("Introduzca el valor entre " + str(min) + " y " + str(max) + ": "))

    while num < min or num > max:
        num = int(input("Introduzca el valor entre " + str(min)  + " y " + str(max) + ": "))
    return num

print(lecturaInterval(valMin,valMax))