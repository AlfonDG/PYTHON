equipo={}
equipo2=dict()
var={1:"SIS1",2:"SIS3",3:None,"SAMUEL":"ESTÁ EN CLASE",(2,3):"TUPLA"}

lista=[]
for i in var:
     print(i,"->",var[i])
     lista.append(i)
print("-----",lista,"-----")

#FOR que recorre los valores de las CLAVES.
for i in var.keys():
    print(i,"->",var[i])
listaPruebaClaves = list(var.keys())
print("----------",listaPruebaClaves,"-----------")

#Printar en un FOR todos los valores de las claves NO LAS CLAVES
for x in var.values():
    print(x)
listaPruebaValores = list(var.values())
print(listaPruebaValores)

#El FOR permite mostrar TODOS los valores claves con valores de diccionario y permite recorrerlos
for clave,valores in var.items():
    print(clave,valores)