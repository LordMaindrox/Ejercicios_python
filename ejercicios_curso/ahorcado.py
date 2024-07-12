import random


def seleccion_aleatoria(lista):
  return random.choice(lista)

def run ():
  frutas = ['melon', 'sandia', 'platano', 'fresa']
  materias = ['metematicas', 'español', 'fisica', 'quimica']
  oportunidades = 0
  jugador = []
  vidas = 3
  

  print('--------------------------------')
  print('Bienvenido al juego del ahorcado')
  print('--------------------------------')
  print(""" Categorias de palabras
  
  1.- frutas
  2.- materias
  """)
  categoria = int(input("Elija una categoria para jugar: "))
  print('--------------------------------')
  if categoria == 1:
    palabra_secreta = seleccion_aleatoria(frutas)
    print('жжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжж')
    print(f'la palabra que quiere adivinar tiene {len(palabra_secreta)} letras ')
    print('Solo cuenta con 3 vidas, cada error resta una')
    print('жжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжж')
    print('\n')
    while vidas > 0 :
      letra = input('Escriba una letra y prueba su suerte: ').lower()
      if letra in palabra_secreta:  
          print("Correcto, la letra si esta en la palabra") 
          jugador.append(letra)
          print('\n')  
      else:
          vidas = vidas - 1
          print(f'La palabra no tiene esa letra, has perdido una vida solo te quedan {vidas} oportunidades')
          print('\n') 
    print('--------------------------------')     
    print('¡Se acabaron las oportunidades!')
    print(f'Las letras que adivinaste son {jugador}')
    adivinar_palabra = input('¿Puedes adivinar la palabra?: ').lower()
    if palabra_secreta == adivinar_palabra:
      print('\n')
      print('♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ')  
      print('ʘ‿ʘ Felicidades ganaste')
    else:
      print('\n')
      print('(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽)(⩾﹏⩽) ') 
      print('(⩾﹏⩽) lo sentimos suerte para la próxima')
  elif categoria == 2: 
    seleccion_aleatoria(materias)
    print(seleccion_aleatoria(materias))


if __name__ == '__main__':
  run()