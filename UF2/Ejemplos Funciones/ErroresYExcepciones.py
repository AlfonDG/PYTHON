#CONTROL DE ERRORES

def control_errores():

    while True:

        try:
            valor=int(input("Entra una edad: "))

            if valor < 0:

                raise Exception

        except ValueError:

            print("No has introducido un número")

        except Exception:

            print("Error")

        # except ZeroDivisionError:
        #
        # print("Estás dividiendo entre 0")

        finally:
             print("FINALLY")

        # else:
        #     print("ELSE")
        #     break

control_errores()