divisas = {"Euro":"€","Dollar":"$","Ien":"¥"}

#La función .title funciona de forma que escribe la primera letra en mayusculas y el resto en minúsuculas
divisa = str(input("Escriba la divisa que deseé: ")).title()

#Realizamos un condicional que permita ver si tenemos la divisa introducida en las keys o claves de los diccionarios
#Finalmente printamos el value en caso de que lo encuentre.
if divisa in divisas.keys():
    print(divisas[divisa])
else:
    print("No, no hemos encontrado la divisa introducida")

