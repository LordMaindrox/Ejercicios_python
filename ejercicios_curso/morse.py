morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',    
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',    
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.',  ')': '-.--.-', ' ': ' '}

morse_inverso = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',   '.': 'E',
    '..-.': 'F',  '--.': 'G',   '....': 'H',  '..': 'I',    '.---': 'J',
    '-.-': 'K',   '.-..': 'L',  '--': 'M',    '-.': 'N',    '---': 'O',
    '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',  '-.--': 'Y',
    '--..': 'Z', 
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
    '-.--.': '(', '-.--.-': ')', ' ': ' '
}

def conversorMorse (palabra):
    list(palabra)
    for letra in palabra:
        print(morse_code[letra], end=" ")

def conversorAlpha(palabra):
    lista=palabra.split(',')
    for letra in lista:
        print(morse_inverso[letra], end=" ")

def esNumero(valor):
    try:
        numero = int(valor)
        return True
    except ValueError:
        return False

print(""" Seleccione lo que desea hacer:  
      1.- De Alfanumérico a Morse
      2.- De Morse a Alfanumérico """)
seleccion = input(" Respuesta:  ")


if esNumero(seleccion):
    if seleccion == '1' or seleccion == '2':
        if seleccion == '1':
            frase = input("Ingrese una palabra ")
            conversorMorse(frase.upper())
        elif seleccion == '2': 
            frase = input("Ingrese código separado por comas \",\" : ")
            conversorAlpha(frase)
    else: 
        print("Selección incorrecta")
else: 
    print("Valor incorrecto")
