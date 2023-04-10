#Creamos un contador que empiece en 0
i = 0

#Creamos un bucle que indique que si el contador sea mayor o igual a 999 (en este caso será 1000 ya que habrá una posiicón de más que cuenta en 0)
while i <= 999:

    #Sumamos el contador en 1 progresivamente
    i += 1

    #Decimos que si el contador es múltiple de 7 lo muestre por pantalla.
    if i % 7 == 0:
        print(i," será múltiple de 7")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)
