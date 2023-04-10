
lista = [1, 2, 3, 4, 5]

def error_lista_numeros ():
    try:
        lista[3]
    except IndexError:
        print("La llista no té tants elements ")
        print("La llista té la següent quantitat de números: ",len(lista),"\nHauries de posar un número entre el 0 i el 4.\nLa llista és la següent: ",lista)

error_lista_numeros()