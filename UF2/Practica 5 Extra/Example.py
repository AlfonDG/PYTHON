def crear_funcio_contador(n):
    def inner():
        for i in range(1, n+1):
            print(i)
    return inner

# create a counter function to count up to 5
contador_5 = crear_funcio_contador(5)
# create a counter function to count up to 10
contador_10 = crear_funcio_contador(10)

# call the functions
contador_5() # counts up to 5
contador_10() # counts up to 10