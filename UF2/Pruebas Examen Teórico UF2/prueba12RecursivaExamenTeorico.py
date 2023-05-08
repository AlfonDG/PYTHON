
def potencia(x,y):

    if y == 0:

        return 1

    else:

        return x * potencia(x, y - 1)

print(potencia(2,2))