frutas = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}

fruta = str(input("Introduzca una fruta: ")).title()

if fruta in frutas.keys():
    peso = float(input("Introduzca el peso: "))
    print(f"El peso de la ***{fruta}*** introducida será","***",peso*frutas[fruta],"***","euros")
else:
    print("No se encuentra esta fruta")