
ex1 = float(input("Introduzca la nota del primer examen: "))

nota = float(input("¿Qué nota quieres sacar durante el trimestre?: "))

primerExamen = 0.20

segundoExamen = 0.80

ex2 = (nota - ex1 * primerExamen) / segundoExamen

print("Para tener un 5 en el trimestre necesitarás sacar un {:>5.1f}".format(ex2)," en el segundo examen")