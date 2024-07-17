import random
def run():
    opciones = ["piedra","papel","tijeras"]
    jugador1 = random.choice(opciones)
    print("jugador 1 elije " +jugador1)
    jugador2 = random.choice(opciones)
    print("jugador 2 elije "+jugador2)

    if ((jugador1 == "piedra") & (jugador2 == "tijeras")):
        print("jugador1 gana")
    elif((jugador1 == "tijeras")& (jugador2 =="papel")):
        print("jugador1 gana")
    elif((jugador1 == "papel")&(jugador2 =="piedra")):
        print("jugador1 gana")
    elif(jugador1 == jugador2):
        print("Empate")
    else:
        print("jugador2 gana")

if __name__ == '__main__':
    run()