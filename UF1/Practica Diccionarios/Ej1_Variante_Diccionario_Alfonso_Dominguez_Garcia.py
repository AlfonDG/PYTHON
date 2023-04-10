divisas = {"Euro":"€","Dollar":"$","Ien":"¥"}

valorMoneda = str(input("Introduzca el símbolo de la moneda: "))

x = False

for i, j in divisas.items():

    if valorMoneda == j:
        print(f"Has introducido el valor {valorMoneda} que equivale al valor {i}")
        x = True
    #NO USAR UN ELSE ya que repetirá en cada momento si lo ha encontrado o no. Por eso hemos creado esta variable semáforo de x = False y en caso de que la encuentre
    #Se inicializa el valor en False hasta que la encuentre en True.
if x == False:
    print("No hemos encontrado el símbolo introducido")