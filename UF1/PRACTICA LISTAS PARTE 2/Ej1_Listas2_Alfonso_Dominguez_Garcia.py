#Crearemos el conjunto de tres listas: listaAlumnos, listaNotas y listaResultados
listaAlumnos = []

listaNotas = []

listaResultados = ["Suspés", "Aprovat", "Bé", "Notable","Excel·lent"]

#En esta variable establecemos la cantidad de alumnos que va a escribir el usuario... En este caso 8 según enunciado.
numeroAlumnos = 8

#Ahora escribimos el bucle WHILE que hasta que el número de alumnos NO sea inferior a 0 no parará de insertar datos.
while numeroAlumnos > 0:

    #Pedimos al usuario los nombres de los alumnos.
    nombreAlumno = str(input("Escriba el nombre del alumno: ")).lower()

    #Añadiremos los nombres de los alumnos a la lista.
    listaAlumnos.append(nombreAlumno)

    #Le pediremos al usuario las notas de cada alumno en formato FLOAT, ya que una nota puede ser decimal.
    notaAlumno = float(input("Escriba la nota del alumno: "))

    #Añadimos las notas del alumno a la lista de notas.
    listaNotas.append(notaAlumno)

    #Decrementamos el contador de alumnos a introducir. Se decrementa de 1 en 1.
    numeroAlumnos -= 1

#Crearemos un bucle FOR para comprobar que accederemos a los elementos de las tres listas
#Y a sus posiciones respectivas.
for i in range(len(listaNotas)):
    #He creado los condicionales que tienen los rangos de las notas de 1 a 4 | De 7 a 8 de 9 a 10
    #Las notas al ser de tipo FLOAT podrá poner decimales y de esta forma entrará en los distintos condicionales.
    if 1 <= listaNotas[i] <= 4:
        print(f"El alumno *{listaAlumnos[i]}* ha obtenido una nota de *{listaResultados[0]}*")
    elif 5.0 <= listaNotas[i] <= 5.9:
        print(f"El alumno *{listaAlumnos[i]}* ha obtenido una nota de *{listaResultados[1]}*")
    elif 6.0 <= listaNotas[i] <= 6.9:
        print(f"El alumno *{listaAlumnos[i]}* ha obtenido una nota de *{listaResultados[2]}*")
    elif 7 <= listaNotas[i] <= 8:
        print(f"El alumno *{listaAlumnos[i]}* ha obtenido una nota de *{listaResultados[3]}*")
    elif 9 <= listaNotas[i] <= 10:
        print(f"El alumno *{listaAlumnos[i]}* ha obtenido una nota de *{listaResultados[4]}*")
    else:
        print("No has establecido una nota correcta")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)