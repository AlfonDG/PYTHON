morse= {
 'A': '.-', 'B': '-...', 'C': '-.-.',
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..', '1': '.----',
 '2': '..---', '3': '...--', '4': '....-',
 '5': '.....', '6': '-....', '7': '--...',
 '8': '---..', '9': '----.', '0': '-----',
 '.': '.-.-.-', ',': '--..--', ':': '---...',
 ';': '-.-.-.', '?': '..--..', '!': '-.-.--',
 '"': '.-..-.', "'": '.----.', '+': '.-.-.',
 '-': '-....-', '/': '-..-.', '=': '-...-',
 '_': '..--.-', '$': '...-..-', '@': '.--.-.',
 '&': '.-...', '(': '-.--.', ')': '-.--.-'
}

codigoMorseInverso = str(input("Introduzca el código morse pero esta vez su símbolo: "))

separacionCodigoMorseInverso = codigoMorseInverso.split()

noEncontrado = True

palabraGenerada = ""

for i in range(len(separacionCodigoMorseInverso)):
    for letras,simbolos in morse.items():
         if separacionCodigoMorseInverso[i] == simbolos:
             print(letras)
             palabraGenerada += letras
             noEncontrado = False
print(f"\nLa frase con las palabras será -> ***{palabraGenerada}***")
if noEncontrado == True:
    print("No hemos encontrado el símbolo")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)