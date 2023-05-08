
def subrutina():

    def sub_subrutina():
        
        nonlocal a

        print(a)

        a = 5

    a = 3

    sub_subrutina()

    print(a)

a = 9

subrutina()

print(a)