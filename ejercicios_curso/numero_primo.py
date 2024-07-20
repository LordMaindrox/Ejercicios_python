def esPrimo(incongnita):
    if incongnita <= 1:
        return False
    for i in range (2,incongnita+1):
        if incongnita % i == 0:
            return False
    return True

def run():
    numero = 1
    esPrimo(numero)
    if esPrimo(numero):
        print(f"{numero} es un número primo.")
    else: 
        print(f"{numero} no es un número primo.")

if __name__ == '__main__':
    run()