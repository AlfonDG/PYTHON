listaAlumnos = []

listaNotas = []

listaResultados = ["Suspés","Suspés","Suspés","Suspés","Suspés","Aprovat","Bé","Notable","Notable","Excel·lent","Excel·lent"]

for i in range(0,2):

    listaNotas.append(float(input("Escriba la nota: ")))

    listaAlumnos.append(str(input("Escriba el nombre del alumno: ")))

n = 8

a = 0

while a < n:

    print(listaAlumnos[a], "ha obtingut un", listaResultados[int(listaNotas[a])])

    a += 1