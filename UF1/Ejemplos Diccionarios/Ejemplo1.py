equipo={}
equipo2=dict()
print(equipo,equipo2)
#--------------------------------Formas de creación de Diccionarios
var={1:"SIS1",2:"SIS3",3:None}
print(var)
#Añadir una clave nueva
var[1]="AMS1"
print(var)
#Si no existe la clave la crea de nuevo
var[11]="AWS1"
print(var)

#Crear la nueva clave
var[500]=var[1]
print(var)

#Añadir a un nuevo diccionario
equipo["SAMUEL"]="ESTÁ EN CLASE"
print(equipo)

