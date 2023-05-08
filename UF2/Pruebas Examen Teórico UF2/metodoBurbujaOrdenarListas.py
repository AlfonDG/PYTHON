listaNotas = [5,9,6,7]

listaAlumnos = ["Alfonso","Cristian","Papá","Mamá"]

def metodo_burbuja(listaNotas,listaAlumnos):


    for i in range(len(listaNotas)):

        for j in range(len(listaNotas) - 1):

            if listaAlumnos[j] < listaAlumnos[j + 1] and listaNotas[j] < listaNotas[j + 1]:

                auxiliarAlumnes = listaAlumnos[j]

                listaAlumnos[j] = listaAlumnos[j + 1]

                listaAlumnos[j + 1] = auxiliarAlumnes

                #Apartado Notas

                auxiliarNotas = listaNotas[j]

                listaNotas[j] = listaNotas[j + 1]

                listaNotas[j + 1] = auxiliarNotas

    return listaAlumnos," -> ", listaNotas

print(metodo_burbuja(listaNotas,listaAlumnos))