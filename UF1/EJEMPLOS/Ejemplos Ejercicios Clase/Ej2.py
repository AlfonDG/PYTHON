num1 = int(input("Escriba el primer número entero PAR: "))

num2 = int(input("Escriba el segundo número entero IMPAR: "))

if num1 % 2 != 0:
    print("No has escrito un número par, ", num1, "no es par!!!")

elif num2 % 2 == 0:
    print("No has escrito un número impar", num2, "es par!!!")


if num1 % num2 == 0:
    print(num1, "es doble de", num2)
else:
    print(num1, "no es doble de", num2)

'''Corrección EN CLASE

if num1 % 2 != 0:
    print("No has escrito un número par, ", num1, "no es par!!!")

if num2 % 2 == 0:
    print("No has escrito un número impar", num2, "es par!!!")

if num1 == 2*num2:
    print(num1, "Es el doble de:", num2)
'''