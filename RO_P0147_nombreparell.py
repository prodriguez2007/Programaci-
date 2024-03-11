# RO_P0147_nombreparell

from random import*
n = int(input("Nombre parell:"))
sortida = False
if n % 2 != 0:
    print("Error")
else:
    while not sortida:
        numero1 = randint(1,1000)
        numero2 = randint(1,1000)
        suma = numero2 + numero1
        if suma == n:
            print(f"Els numeros aleatoris són {numero1} i {numero2}")
            print("La suma és",n)
            sortida = True    