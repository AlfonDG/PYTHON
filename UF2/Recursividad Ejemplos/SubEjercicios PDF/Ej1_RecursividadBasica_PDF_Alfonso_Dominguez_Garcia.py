__author__ = "Alfonso Domínguez García"
__copyright__="Copyright © 2023 Alfonso Domínguez García"

base = 5

exponente = 3

def elevado_a_recursiva(base,exponente):

    if exponente == 0:

        return 1

    elif exponente == 1:

        return base

    else:

        return base * elevado_a_recursiva(base,exponente - 1)

print(elevado_a_recursiva(base,exponente))

print("")

print(__author__)
print(__copyright__)