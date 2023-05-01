import random


personajes = {

    "jugador": {

        "nombre": "Jugador",
        "raza": "humano",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 10, "destreza": 5, "inteligencia": 2, "carisma": 3

        },

        "inventario": ["espada", "escudo", "posiciones"],

    },

    "enemigo1": {

        "nombre": "Ogro",
        "raza": "ogro",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 8, "destreza": 3, "inteligencia": 1, "carisma": 1

        },

        "inventario": ["garrote"],

    },

    "enemigo2":{

        "nombre":"Mago oscuro",
        "raza":"humano",
        "clase":"mago",

        "habilidades":{
            "fuerza":2,"destreza":4,"inteligencia":10,"carisma":5
        },

        "inventario": ["varita mágica", "libro de hechizos"]

    },

}

monstruos = {

    "goblin": {"nivel":1,
               "vida":10,
               "ataque":5,
               "defensa":5,
               "habilidades":["ataque normal","invocar esqueletos"]

               },

    "rata": {"nivel":2,
               "vida":20,
               "ataque":10,
               "defensa":10,
               "habilidades":["ataque normal","invocar esqueletos"]

               },

    "dragón": {"nivel":5,
               "vida":50,
               "ataque":20,
               "defensa":20,
               "habilidades":["ataque normal","invocar esqueletos"]

               },
}

nomColumnes=("nombre","raza","clase","fuerza","destreza","inteligencia","carisma","inventari")

relacio_personajes_monstruos = {"Gandalf":"dragon",
                                "Aragorn":"rata",
                                "Legolas":"troll",
                                "Frodo":"goblin",
                                "Gimli":"rata"
                                }

print("\n---Apartado B Examen UF2---\n")

#Apartado B (Completado)
def mostrarDades(personajes):

    margenes = "=" * 120

    print(margenes)

    for i in nomColumnes:

        print(i.center(12) + " | ", end="")

    print("")

    print(margenes)

    for claves,valores in personajes.items():

        print("")

        for keys,values in personajes[claves].items():

            if keys == "habilidades":

                fuerza = valores["habilidades"]["fuerza"]

                destreza = valores["habilidades"]["destreza"]

                inteligencia = valores["habilidades"]["inteligencia"]

                carisma = valores["habilidades"]["carisma"]

                print(str(fuerza).center(16), end=" ")
                print(str(destreza).center(16), end=" ")
                print(str(inteligencia).center(16), end=" ")
                print(str(carisma).center(16), end=" ")

            else:
                print(str(values).center(12), end=" ")

    print("\n" + "\n" + margenes)

mostrarDades(personajes)


print("\n---Apartado C Examen UF2---\n")

#Apartado C (Completado)
def inteligenciaOrder(personajes):

    listaPersonajes = []

    listaInteligenciaPersonajes = []

    for clavePers, valoresPers in personajes.items():

        listaInteligenciaPersonajes.append(valoresPers["habilidades"]["inteligencia"])

        listaPersonajes.append(valoresPers["nombre"])

    lenPersonajes = len(listaPersonajes)

    for i in range(lenPersonajes):

        for j in range(0, lenPersonajes - i - 1):

            if listaInteligenciaPersonajes[j] > listaInteligenciaPersonajes[j + 1] and listaPersonajes[j] > listaPersonajes[j + 1]:

                auxiliarListaInteligencia = listaInteligenciaPersonajes[j]

                listaInteligenciaPersonajes[j] = listaInteligenciaPersonajes[j + 1]

                listaInteligenciaPersonajes[j + 1] = auxiliarListaInteligencia

                auxiliarListaPersonajes = listaPersonajes

                listaPersonajes[j] = listaPersonajes[j + 1]

                listaPersonajes[j + 1] = listaPersonajes[j]

                listaPersonajes[j] = auxiliarListaPersonajes

        return listaPersonajes,listaInteligenciaPersonajes

print(inteligenciaOrder(personajes))


print("\n---Apartado D Examen UF2---\n")

#Apartado D (Completado)

def personatgesOrder(personajes,monstruos,relacio_personajes_monstruos):

    personajesOrdenados = sorted(personajes.items(),key=lambda x: x[1]["habilidades"]["destreza"], reverse=True)

    listaMosntruos = []

    for clave,valor in relacio_personajes_monstruos.items():

        listaMosntruos.append(valor)

    for i in range(len(personajesOrdenados)-1,-1,-1):

        if listaMosntruos[i] or personajesOrdenados[i][0] == "rata":

            print(personajesOrdenados[i])

personatgesOrder(personajes,monstruos,relacio_personajes_monstruos)

print("\n---Apartado F Examen UF2---\n")

#Apartado F (Completado)

def combate(personajes, monstruos):

    numeroFuerzaMonstruo = random.randint(0,50)

    listaMonstruos = []

    listaPersonajes = []

    listaFuerzaInventarioPersonaje = []

    fuerzaMonstruo = numeroFuerzaMonstruo


    for claveMons,valorMons in monstruos.items():

        listaMonstruos.append(claveMons)

    for clavePers,valorPers in personajes.items():

        listaPersonajes.append(valorPers["nombre"])

        listaFuerzaInventarioPersonaje.append(len(valorPers["inventario"]) * valorPers["habilidades"]["fuerza"])

    personajesAleatorios = random.choice(listaPersonajes)

    monstruosAleatorios = random.choice(listaMonstruos)

    print(f"Se ha seleccionado de forma aleatoria el nombre del personaje -> {personajesAleatorios}")

    print(f"Se ha seleccioando de forma aleatorio el nombre del monstruo -> {monstruosAleatorios}")

    print(f"\nPor lo tanto se está enfrentando actualmente el personaje -> **{personajesAleatorios}** VS el monstruo **{monstruosAleatorios}**")

    if personajesAleatorios and valorPers["inventario"] == "varita mágica":

        print("Hemos enocntrado que el personaje con el valor {}")

        listaFuerzaInventarioPersonaje *= 3

        print(f"La fuerza del personaje **{listaPersonajes}** definitiva será igual a -> **{listaFuerzaInventarioPersonaje}**")

    elif monstruosAleatorios and valorMons["habilidades"] == "aliento de fuego":

        fuerzaMonstruo *= 2

        print(f"La fuerza del monstruo **{listaMonstruos}** definitiva será igual a -> **{fuerzaMonstruo}**")

combate(personajes, monstruos)

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez García"

print(autor)
print(copy)