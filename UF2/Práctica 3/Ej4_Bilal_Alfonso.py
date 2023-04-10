llista = ["Bilal", "Rayan", "Alfonso", "Pau", "Albert", "Dani"]
element=input("Introdueix un alumne: ").title()
def afegir_una_vez(llista,element):
    try:
        if element in llista:
            raise ValueError
        else:
            llista.append(element)
            print(llista)
    except ValueError:
        print("Error: Impossible afegir elements duplicats => ",element)
    return llista
afegir_una_vez(llista,element)
