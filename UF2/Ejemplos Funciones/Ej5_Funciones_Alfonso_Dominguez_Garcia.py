caracterU = input("Introduzca lo que deseé número o letra: ")

def esDigit(caracter):

    if len(caracter) == 1:

        if caracter.isalpha():

            return 1

        elif caracter.isdigit():

            return 0
    else:
        return "No ha escrito una letra o un número"
    #return - 1

print(esDigit(caracterU))

if esDigit(caracterU) == 0:
    print("Es un número")

elif esDigit(caracterU) == 1:
    print("Es una letra")

else:
    print("Error")