def funcion():

    a = 88

    print("FUNCIÓN:", a)

    a = a + 7

    print("a=", a)

    def funcion2():
        nonlocal a
        a=115
        print("Dentro función 2:",a)
    funcion2()
    print("Fuera de función 2:",a)


a = 77

funcion()

print("Variable global externa a funcón",a)