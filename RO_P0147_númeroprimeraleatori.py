#RO_P0147_numeroaletoriprimer
from random import*
salida = False
    
while not salida:
    numero1 = randint(1,100)
    numero = 2
    while numero1 % numero != 0 and numero1 != numero:
        numero = 1 + numero
    if numero1 == numero:
        print(numero1)
        salida = True
        
        
        