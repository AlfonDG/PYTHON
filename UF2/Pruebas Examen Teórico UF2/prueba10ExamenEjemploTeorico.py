
string = "alfonso"

def contador_strings(string):

    contador = 0

    if len(string) == 0:

        return 1

    else:

        return contador + contador_strings(string[:-1])

print(contador_strings(string))