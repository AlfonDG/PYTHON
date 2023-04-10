#PARAMETROS POR OMISIÓN
def suma(b,c=66,d=99,*a):

    print(b)

    print(c)

    print(d)

    print(a)

    s = b

    for i in a:

        s+= i

    return s

    #print(type(a))

print(suma(8,5,7,7))

print(suma(8,3,2,3,1,900))