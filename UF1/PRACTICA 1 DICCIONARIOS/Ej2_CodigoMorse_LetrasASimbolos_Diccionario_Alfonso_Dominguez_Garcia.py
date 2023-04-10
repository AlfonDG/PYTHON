morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
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
 '&': '.-...', '(': '-.--.', ')': '-.--.-'}

codigoMorse = str(input("Por favor, introduzca su palabra y la pasaremos a código morse: ")).upper()

letraNoEncontrada = True

for i in codigoMorse:
    for letra in morse.keys():
        if i == letra:
            print(morse[i])
            letraNoEncontrada = False
if letraNoEncontrada == True:
    print("No hemos encontrado la letra o los carácteres introducidos")

print("")
autor = __author__ = "Alfonso Domínguez García"
copy = __copyright__="Copyright © 2022 Alfonso Domínguez García"

print(autor)
print(copy)
