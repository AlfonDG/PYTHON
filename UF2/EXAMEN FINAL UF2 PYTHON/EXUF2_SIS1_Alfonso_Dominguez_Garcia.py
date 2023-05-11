import random

monstres = {
    'goblin': [1,10,5, 5,['ataque normal', 'vuelo']],
    'rata': [ 2, 20,10, 10, ['ataque normal', 'invocar esqueletos'] ],
    'dragon': [ 5,50, 20,20, ['ataque normal', 'aliento de fuego', 'vuelo']],
    'troll': [7,77,30,10, ['aliento de fuego']]
}

relacio_personajes_monstres = [
    ("Gandalf", "dragon",'vuelo'),
    ("Aragorn", "rata",'invocar esqueletos'),
    ("Legolas", "troll",'aliento de fuego'),
    ("Frodo", "goblin",'vuelo'),
    ("Gimli", "rata",'invocar esqueletos'),
    ("Gandalf", "rata",'ataque normal'),
    ("Legolas", "rata",'invocar esqueletos'),
]
personajes =  [
    {"nombre": "Gandalf",
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
    {
        "nombre":"Aragorn",
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
    {
        "nombre": "Legolas",
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
     {
        "nombre": "Frodo",
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
     {
        "nombre": "Gimli",
        "raza": "ogro",
        "clase": "guerrero",
        "habilidades": {
            "fuerza": 3,
            "destreza": 4,
            "inteligencia": 9,
            "carisma": 8
        },
        "inventario": ["libro de hechizos"]
    }
]
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

margenes = "=" * 90

print(margenes)


print("\n-------APARTADO B)-----\n")


def mostrarDades(personajes):
    listaNombres = []

    listaRaza = []

    listaClase = []

    listaFuerza = []

    listaDestreza = []

    listaInteligencia = []

    listaCarisma = []

    listaInventario = []

    for valoresPers in personajes:
        listaNombres.append(valoresPers["nombre"])

        listaRaza.append(valoresPers["raza"])

        listaClase.append(valoresPers["clase"])

        listaFuerza.append(str(valoresPers["habilidades"]["fuerza"]))

        listaDestreza.append(str(valoresPers["habilidades"]["destreza"]))

        listaInteligencia.append(str(valoresPers["habilidades"]["inteligencia"]))

        listaCarisma.append(str(valoresPers["habilidades"]["carisma"]))

        listaInventario.append(str(valoresPers["inventario"]))

    margenesTabla = "-" * 190

    print(margenesTabla)

    for i in nomColumnes:
        print(i.center(20), end=" | ")

    print("")

    print(margenesTabla)

    for x in range(len(listaNombres)):
        print(listaNombres[x].center(20), listaRaza[x].center(25), listaClase[x].center(15), listaFuerza[x].center(30),
              listaDestreza[x].center(20)
              , listaInteligencia[x].center(15), listaCarisma[x].center(30), listaInventario[x].center(20))

    print(margenesTabla)


mostrarDades(personajes)

print(margenes)

print("\n----APARTADO C)-----\n")

def inventariOrder(personajes):

    listaInventario = []

    for clave in personajes:

        listaInventario.append(clave["inventario"][0])

    for i in range(len(listaInventario)):

        for j in range(len(listaInventario) - 1):

            if listaInventario[j] < listaInventario[j + 1]:

                auxiliarInventario = listaInventario[j]

                listaInventario[j] = listaInventario[j + 1]

                listaInventario[j + 1] = auxiliarInventario
                
    return f"La lista ordenada por el primer elemento del inventario será -> ",listaInventario,personajes

    print(personajes)

print(inventariOrder(personajes))

print("")

print(margenes)

print("\n----APARTADO E)----\n")

def drago():

    caminos = random.randint(1,10)

    if caminos % 2 == 1 and caminos != 3:

        return 10 + drago()

    elif caminos % 2 == 0 and caminos != 10:

        return 2 + drago()

    elif caminos == 3:

        return 7 + drago()

    elif caminos == 10:

        return 1

minutosTotalesDragon = drago()

print(f"El dragón habrá tardado un total de **{minutosTotalesDragon}** minutos en salir del laberinto")

print("")

print(margenes)