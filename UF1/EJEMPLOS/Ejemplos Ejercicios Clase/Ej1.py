ph = int(input("Escriba el PH del agua de su pescadería: "))

if ph < 7:
    print("Su PH del agua de la pescadería será ácida")
elif ph == 7:
    print("Su PH del agua de la pescadería será neutra")
elif ph > 7:
    print("Su PH del agua de su pescadería es de medio básico")
else:
    print("No has escrito una operación correcta")
