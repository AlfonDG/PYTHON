import random

censoImperio={
"AR1":{"nombre":"Claudia","region":"Roma","edad":23,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"AD3":{"nombre":"Maximo","region":"Hispania","edad":30,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AC2":{"nombre":"Marco","region":"Hispania","edad":28,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AV6":{"nombre":"Julius","region":"Roma","edad":35,"sexo":"H","categoría":"césar","fuerza":random.uniform(50,200)},
"SS5":{"nombre":"Augustus","region":"Hispania","edad":21,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"WQ6":{"nombre":"Eugenia","region":"Hispania","edad":28,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"JU8":{"nombre":"Anastacia","region":"Hispania","edad":17,"sexo":"I","categoría":"soldado","fuerza":random.uniform(50,200)},
"DF5":{"nombre":"Aurelia","region":"Hispania","edad":20,"sexo":"M","categoría":"pueblo","fuerza":random.uniform(50,200)},
"BR1":{"nombre":"Antistia","region":"Roma","edad":16,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"KR9":{"nombre":"Apolonia","region":"Roma","edad":25,"sexo":"I","categoría":"centurión","fuerza":random.uniform(50,200)},
"KH7":{"nombre":"Acucia","region":"Roma","edad":29,"sexo":"M","categoría":"centurión","fuerza":random.uniform(50,200)},
"XH4":{"nombre":"Titus","region":"Roma","edad":39,"sexo":"I","categoría":"pueblo","fuerza":random.uniform(50,200)},
"KA2":{"nombre":"Aurelio","region":"Roma","edad":15,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
"MJ8":{"nombre":"Tiberius","region":"Roma","edad":22,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
}

recuentoCategoriaCenturion = 0

recuentoCategoriaSoldado = 0

recuentoCategoriaPueblo = 0

recuentoCategoriaCesar = 0

categoriaIntroducir = str(input("\nIntroduzca la categoría que deseé ver en el Censo Romano: ")).lower()

for datosPersona in censoImperio.values():

    categoriaCenso = datosPersona["categoría"]

    while categoriaIntroducir != categoriaCenso:

        categoriaIntroducir = str(input("\nIntroduzca la categoría que deseé ver en el Censo Romano: ")).lower()

    if categoriaCenso == categoriaIntroducir:

        if categoriaCenso == "centurión":

            print("\n Nombre:", datosPersona["nombre"], "\n",
                    "Región:", datosPersona["region"], "\n",
                    "Edad:", datosPersona["edad"], "\n",
                    "Sexo:", datosPersona["sexo"], "\n",
                    "Categoría:", datosPersona["categoría"], "\n")
            recuentoCategoriaCenturion += 1

        elif categoriaCenso == "soldado":
            print("\n Nombre:", datosPersona["nombre"], "\n",
                    "Región:", datosPersona["region"], "\n",
                    "Edad:", datosPersona["edad"], "\n",
                    "Sexo:", datosPersona["sexo"], "\n",
                    "Categoría:", datosPersona["categoría"], "\n")
            recuentoCategoriaSoldado += 1

        elif categoriaCenso == "césar":
            print("\n Nombre:", datosPersona["nombre"], "\n",
                    "Región:", datosPersona["region"], "\n",
                    "Edad:", datosPersona["edad"], "\n",
                    "Sexo:", datosPersona["sexo"], "\n",
                    "Categoría:", datosPersona["categoría"], "\n")
            recuentoCategoriaCesar += 1

        elif categoriaCenso == "pueblo":
            print("\n Nombre:", datosPersona["nombre"], "\n",
                    "Región:", datosPersona["region"], "\n",
                    "Edad:", datosPersona["edad"], "\n",
                    "Sexo:", datosPersona["sexo"], "\n",
                    "Categoría:", datosPersona["categoría"], "\n")
            recuentoCategoriaPueblo += 1

        pulsarTecla = input("Pulsa una tecla para continuar...\n")

print(f"El recuento total de personas con categoría CENTURIÓN son -> {recuentoCategoriaCenturion}")
print(f"El recuento total de personas con categoría CÉSAR son -> {recuentoCategoriaCesar}")
print(f"El recuento total de personas con categoría PUEBLO son -> {recuentoCategoriaPueblo}")
print(f"El recuento total de personas con categoría SOLDADO son -> {recuentoCategoriaSoldado}")