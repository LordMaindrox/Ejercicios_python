import random
nivel_facil = 10
nivel_dificil = 5


def bienvenida():
  print('------------------------------------------------')
  print('Bienvenido al juego de:')
  print("""
__________.__                       
\______   \__| ____    ____   ____  
 |    |  _/  |/    \  / ___\ /  _ \ 
 |    |   \  |   |  \/ /_/  >  <_> )
 |______  /__|___|  /\___  / \____/ 
        \/        \//_____/         
  """)
  
  print('------------------------------------------------')
  print(""" Elige el nivel 
  
  1.- Fácil
  2.- Difícil
  """)
  print('------------------------------------------------')

def categoria():
  categoria = int(input("Elija una categoria para jugar: "))
  if categoria == 1:
    return nivel_facil
  elif categoria == 2: 
    return nivel_dificil


def modo_juego(categoria):

  def numero_secreto():
    secreto = random.randint(1,100)
    return secreto

def turno_jugador(numero, vida):
 
  while vida > 0:
    print('жжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжж')
    tiro = int(input("Digite un número entre 1 y 100: "))
    print('жжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжжж')
    print('\n')
    if tiro == numero:
      print('\n')
      print('♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ♥‿♥ ') 
      return print('ʘ‿ʘ Felicidades ganaste ʘ‿ʘ')
    else: 
      vida = vida -1
      if vida == 0:
        pass
      elif tiro > numero:
        print(f'Has perdido una vida te quedan {vida} intenta de nuevo')
        print(" El númeor que buscas es menor")
      elif tiro < numero:
        print(f'Has perdido una vida te quedan {vida} intenta de nuevo')
        print(" El númeor que buscas es mayor")
  print("Las vidas se han terminado, intenta de nuevi")


def run ():
  
  bienvenida()
  vida = categoria()
  print(f'Ok,  tienes {vida} vidas')
  adivina = numero_secreto()
  print(adivina)
  turno_jugador(adivina,vida)


if __name__ == '__main__':
  run()