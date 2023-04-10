divisorU = int(input("Introduzca el valor de divisor: "))

dividendU = int(input("Introduzca el valor del Dividend: "))

def calculaResidu(dividend,divisor):

    if divisor != 0:

        operacion = divisor % dividend

        return operacion

    elif divisor == 0:
        return "Error, no puede usar números que sean 0 para dividr"

print(calculaResidu(dividendU,divisorU))