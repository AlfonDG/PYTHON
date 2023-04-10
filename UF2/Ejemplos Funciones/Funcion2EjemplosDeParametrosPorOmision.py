def funcion2(parametroFijo,*tupla,**diccionario):

    print(parametroFijo)
    print(tupla)
    print(diccionario)

funcion2(44,"Saul","Albert",clave1="Bilal",clave2="Unax")

def diccionario(**diccionario):

    return diccionario

print(diccionario(nombre="Alfonso",dni="48064936L"))