from operaciones_matematicas import *

print('\nsumar =', sumar(num1, num2))
print('restar =', restar(num1, num2))
print('multiplicar =', multiplicar(num1, num2))
print('dividir =', dividir(num1, num2))

#Finalmente para que funcione este último apartado debemos de importar el módulo de operacions_matematicas de la siguiente forma
#Realizamos un from operaciones_matematicas import sumar,restar,multiplicar,dividir de esta forma seleccionamos cada función que deseamos printar por pantalla
#Solamente tendremos que poner el nombre de las funciones que hayan dentro del módulo operaciones_matematicas sin necesidad de llamar a este módulo.

#Otra cosa que podemos hacer es llamar directamente al módulo "operaciones_matematicas" que se encuentra justo en el package "matemàticas"
#Entonces si hacemos lo siguiente "from operaciones_matematicas import *" All nos permitirá importar todos los valores de las funciones como son
#sumar,restar,multiplicar y dividir que se encuentra dentro del módulo de "operaciones_matematicas" y podremos usarlas.