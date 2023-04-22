#Primero creamos la string de Pizza en formato str() tal y como indica en la práctica.
string = "Pizza"

#Ahora crearemos la función "dar_vuelta" que permitirá pasar como argumento la función "string"
def dar_vuelta(string):

    #Ahora crearemos la variable "darVueltaLambda" que lo que hará será pasar la string de x que será igual a la variable "string"
    #Y lo que nos permitirá será devovler la string al revés
    darVueltaLambda = lambda x: x[::-1]

    #Finalmente tendremos que realizar el return de "darVueltaLambda" y le pasaremos como argumento la variable string ya que la sustituiremos
    #por la variable de x
    return darVueltaLambda(string)

#Finalmente printamos toda la variable más el argumento de string.
print(dar_vuelta(string))

print("")
autor = __author__ = "Alfonso Domínguez"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez"

print(autor)
print(copy)