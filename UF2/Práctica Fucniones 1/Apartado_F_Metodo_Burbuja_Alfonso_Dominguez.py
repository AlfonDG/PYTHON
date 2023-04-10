alumnos = ["Pere","Pau","Anna","Andrea","Pol","Nil","Montserrat","Gerard"]

notas = [4.3, 5.6, 5.9, 9.7, 2.6, 6.8, 8.8, 2.4]

def ordena_alumnes(alumnos, notas):

    for i in range(len(notas)):

        for j in range(len(notas) - 1):

            if notas[j] < notas[j + 1]:

                #Oredenación de los elementos de la lista mediante método Burbuja

                auxiliarNotas = notas[j]

                notas[j] = notas[j + 1]

                notas[j + 1] = auxiliarNotas

                #Método Burbuja aplicado tanto para la lista de alumnos también.

                auxiliarAlumnos = alumnos[j]

                alumnos[j] = alumnos[j + 1]

                alumnos[j + 1] = auxiliarAlumnos

    #Devolvemos ambas listas tanto "alumnos" como "notas" de forma ordenada.
    return alumnos,"->", notas

print(ordena_alumnes(alumnos,notas))

print("")
autor = __author__ = "Alfonso Domínguez & Rayan Haizour"
copy = __copyright__="Copyright © 2023 Alfonso Domínguez & Rayan Haizour"

print(autor)
print(copy)