numeroEntero = int(input("Escriba el número Entero: "))

#Bucle WHILE que permitirá controlar si el número establecido es negativo solamente
while numeroEntero < 0:
    print("Ha escrito un número negativo.","\n")
    numeroEntero = int(input("Vuelva a escribir el número Entero: "))

#Creamos la variable sumaNumeros que permitirá sumar todos los números en el intervalo
sumaNumeros = 0

#Primero haremos un FOR que recorrerá el intervalo de números de 0 hasta numEntero que será el número que quiera el usuario
for i in range(0,numeroEntero):
    sumaNumeros += i
    '''print(i) -> Este PRINT i me mostrará los números que hay de 0 hasta el número del usuario'''
    #Crearemos un condicional que diga que si la suma de los valores de i superen el número entero que haya establecido el usuario
    #Mostraremos la suma de ese número sin el último dígito y saldrá el resultado.
    if sumaNumeros > numeroEntero:
        sumaNumeros -= i
        #Realizamos un BREAK para forzar la salida del bucle y de etsta forma que nos muetsre la suma.
        break

    #Printamos la i al final de bucle FOR ya que si entra en el condicional MOSTRARÁ la suma de los números que hay en el intervalo sin superar el número máximo.
    print(i)

#Finalmente mostramos la suma de los números
print(f"La suma total será {sumaNumeros} ya que el siguiente número ha superado el límite que sería {numeroEntero}")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)