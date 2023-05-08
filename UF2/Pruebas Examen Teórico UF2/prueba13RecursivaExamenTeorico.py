
def producte_numeros(x,y):

    if y == 0:

        return 1

    else:

        return x + producte_numeros(x, y - 1)

print(producte_numeros(2,3))