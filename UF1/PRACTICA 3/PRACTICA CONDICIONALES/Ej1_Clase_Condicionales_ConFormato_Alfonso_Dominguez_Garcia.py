num = float(input("Escriba un número: "))

num2 = float(input("Escriba el segundo número: "))

suma = num + num2

resta = num - num2

multiplicar = num * num2

if num2 <= 0:
    print("No se puede dividir entre cero")

dividir = num / num2

#if num2 != 0:
 #   dividir = num / num2
#else:
 #   print("ERROR: NO PUEDO DIVIDIR ENTRE CERO")


print(f"La suma será {suma:>10.3f}\nLa resta será {resta:>10.3f}\nLa multiplicación será {multiplicar:>10.3f}\nLa división será {dividir:>10.3f}")
print("")
print("SUMA:".ljust(8) + " {:>10.3f}".format(suma))
print("")
print("La suma será {0:>10.3f}\nLa resta será {1:>10.3f}\nLa multiplicacion será {2:>10.3f}\nLa división será {3:>10.3f}".format(suma,resta,multiplicar,dividir))


print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)