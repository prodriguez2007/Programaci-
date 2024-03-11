# Numero auri
from random import*
def primo():
    salida = False
    while not salida:
        numero1 = randint(1,100)
        numero2 = randint(1,100)
        suma = numero2 + numero1
        numero = 2
        while suma % numero != 0 and suma != numero:
            numero = 1 + numero
            if numero == suma:
                print("Número aleatori 1:", numero1)
                print("Número aleatori 2:", numero2)
                print(suma)
                salida = True


