import random

monstruos = {
    'goblin': {
        'nivel': 1,
        'vida': 10,
        'ataque': 5,
        'defensa': 5,
        'habilidades': ['ataque normal', 'vuelo']
    },
    'rata': {
        'nivel': 2,
        'vida': 20,
        'ataque': 10,
        'defensa': 10,
        'habilidades': ['ataque normal', 'invocar esqueletos']
    },
    'dragon': {
        'nivel': 5,
        'vida': 50,
        'ataque': 20,
        'defensa': 20,
        'habilidades': ['ataque normal', 'aliento de fuego', 'vuelo']
    },
    'troll': {
        'nivel': 7,
        'vida': 77,
        'ataque': 30,
        'defensa': 10,
        'habilidades': ['aliento de fuego']
    }
}
relacio_personajes_monstruos = {
    "Gandalf": "dragon",
    "Aragorn": "rata",
    "Legolas": "troll",
    "Frodo": "goblin",
    "Gimli": "rata"
}
personajes = {
    "Gandalf": {
        "nombre": "Jugador",
        "raza": "humano",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 10,
            "destreza": 5,
            "inteligencia": 2,
            "carisma": 3
        },
        "inventario": ["espada", "escudo", "pociones"]
    },
    "Aragorn": {
        "nombre": "Ogro",
        "raza": "ogro",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 80,
            "destreza": 3,
            "inteligencia": 1,
            "carisma": 1
        },
        "inventario": ["garrote"]
    },
    "Legolas": {
        "nombre": "Mago oscuro",
        "raza": "humano",
        "clase": "mago",
        "habilidades": {
            "fuerza": 200,
            "destreza": 4,
            "inteligencia": 10,
            "carisma": 5
        },
        "inventario": ["varita magica", "libro de hechizos"]
    },
    "Frodo": {
        "nombre": "Brujo",
        "raza": "ogro",
        "clase": "mago",
        "habilidades": {
            "fuerza": 12,
            "destreza": 6,
            "inteligencia": 20,
            "carisma": 1
        },
        "inventario": ["varita magica", "libro de hechizos"]
    },
    "Gimli": {
        "nombre": "Dragon",
        "raza": "ogro",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 3,
            "destreza": 1,
            "inteligencia": 9,
            "carisma": 8
        },
        "inventario": ["libro de hechizos"]
    }
}
'''
Gandalf s'ha enfrontat a un dragó, Aragorn a una rata, Legolas a un troll, 
Frodo a un goblin i Gimli a una rata.
'''
relacion_monstruos_personajes = {
    "Gandalf": "dragon",
    "Aragorn": "rata",
    "Legolas": "troll",
    "Frodo": "goblin",
    "Gimli": "rata"
}

nomColumnes=("nombre","raza","clase","fuerza","destreza","inteligencia","carisma", "inventari")

#--------------------------------------------------------------------------------------------------------------------
print("\n---Apartado B Examen UF2---\n")

#Apartado B (Completado)
def mostrarDades(personajes):

    margenes = "=" * 182

    print(margenes)

    for i in nomColumnes:

        print(i.center(21) + "|", end="")

    print("")

    print(margenes)

    for claves,valores in personajes.items():

        print("")

        for keys,values in personajes[claves].items():

            if keys == "nombre":

                nombrePersonaje = claves

                print(str(nombrePersonaje).center(18),end="")

            elif keys == "habilidades":

                fuerza = valores["habilidades"]["fuerza"]

                destreza = valores["habilidades"]["destreza"]

                inteligencia = valores["habilidades"]["inteligencia"]

                carisma = valores["habilidades"]["carisma"]

                print(str(fuerza).center(21), end=" ")
                print(str(destreza).center(21), end=" ")
                print(str(inteligencia).center(21), end=" ")
                print(str(carisma).center(21), end=" ")

            else:
                print(str(values).center(23), end="")

    print("\n" + "\n" + margenes)

mostrarDades(personajes)

#----------------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------------------------------

print("\n----APARTADO E Examen UF2---\n")

#Apartado E (completado)

def mouse():

    caminos = random.randint(1,3)

    if caminos == 1:

        return 3 + mouse()

    elif caminos == 2:

        return 5 + mouse()

    elif caminos == 3:

        return  7

minutosFinales = mouse()

print(mouse())

print("El monstruo rata", "con poderes", monstruos["rata"],"ha tardado en salir de la jaula un total de", minutosFinales, "minutos")

#-------------------------------------------------------------------------------------------------------------

print("\n---Apartado F Examen UF2---\n")

# Apartado F (Completado)

def combate(personajes, monstruos):
    numeroFuerzaMonstruo = random.randrange(0, 50)

    listaMonstruos = []

    listaPersonajes = []

    personajeSeleccionadoAzar = ""

    monstruoSeleccionadoAzar = ""

    fuerzaInventarioPersonaje = 0

    fuerzaMonstruo = numeroFuerzaMonstruo

    for claveMons, valorMons in monstruos.items():
        listaMonstruos.append(claveMons)

    for clavePers, valorPers in personajes.items():
        listaPersonajes.append(clavePers)

        fuerzaInventarioPersonaje = (len(valorPers["inventario"]) * valorPers["habilidades"]["fuerza"])

    personajeSeleccionadoAzar = random.choice(listaPersonajes)

    monstruoSeleccionadoAzar = random.choice(listaMonstruos)

    print(f"Se ha seleccionado de forma aleatoria el nombre del personaje -> {personajeSeleccionadoAzar}")

    print(f"Se ha seleccioando de forma aleatorio el nombre del monstruo -> {monstruoSeleccionadoAzar}")

    print(f"\nPor lo tanto se está enfrentando actualmente el personaje -> **{personajeSeleccionadoAzar}** VS el monstruo **{monstruoSeleccionadoAzar}**")

    if personajeSeleccionadoAzar and valorPers["inventario"] == "varita mágica":

        print("Hemos enocntrado que el personaje con el valor {}")

        fuerzaInventarioPersonaje *= 3

        print(f"La fuerza del personaje **{listaPersonajes}** definitiva será igual a -> **{fuerzaInventarioPersonaje}**")

    elif monstruoSeleccionadoAzar and valorMons["habilidades"] == "aliento de fuego":

        fuerzaMonstruo *= 2

        print(f"La fuerza del monstruo **{listaMonstruos}** definitiva será igual a -> **{fuerzaMonstruo}**")

    while fuerzaInventarioPersonaje > 0 and fuerzaMonstruo > 0:

        fuerzaMonstruo -= int(personajes[personajeSeleccionadoAzar]["habilidades"]["fuerza"])

        if fuerzaMonstruo <= 0:
            print(f"\nEl personaje **{personajeSeleccionadoAzar}** ha perido contra el monstruo **{monstruoSeleccionadoAzar}**.")

            break

        fuerzaMonstruo -= int(personajes[personajeSeleccionadoAzar]["habilidades"]["fuerza"])

        if fuerzaMonstruo <= 0:
            print(f"\nEl personaje **{personajeSeleccionadoAzar}** ha ganado la batalla frente al monstruo **{monstruoSeleccionadoAzar}**")

combate(personajes, monstruos)

#-------------------------------------------------------------------------------------------------------------------------------------------------ç

print("\n---Apartado A Examen UF2---\n")

#Apartado A (Completado)

def crea_personatje(personajes):

    listaRaza = []

    listaClases = []

    for clavePers, valoresPers in personajes.items():

        listaRaza.append(valoresPers["raza"])

        listaClases.append(valoresPers["clase"])

    nombrePersonaje = str(input("Introduzca el nombre del personaje a añadir: "))

    nombreClave = str(input("Introduzca el valor en CLAVE del nombre del personaje: "))

    raza = str(input("Inserte ahora el valor de la RAZA del personaje: "))

    clase = str(input("Inserte el valor de la CLASE del personaje: "))

    nivel = int(input("Introduzca un valor para el NIVEL del personaje: "))

    vida = int(input("Introduzca el valor de la VIDA que tendrá el personaje: "))

    def checkCategory(clase,raza):

        try:

            if clase not in listaClases:

                return False

            elif raza not in listaRaza:

                return False

            else:

                return True

        finally:
            print("El codigo checkCategori se ha ejecutado de forma correcta")

    print(checkCategory(clase,raza))


    def checkNum(nivel,vida):

        try:

            if nivel > 10 or nivel < 1:

                return False

            elif vida > 100 or vida < 0:

                return False

        finally:

            print("El codigo checkNum se ha ejecutado de forma correcta")

        print(checkNum(nivel,vida))

    personajes[nombrePersonaje] = {"nombre":nombreClave,"raza":raza,"clase":clase,"nivel":nivel,"vida":vida}

crea_personatje(personajes)

print(personajes)

#--------------------------------------------------------------------------------------------------------

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez García"

print(autor)
print(copy)