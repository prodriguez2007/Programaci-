# RO_P0148_Dado
from random import* 

n = int(input("Nombre d'intents:"))
diners = 0

for i in range(n):
    dau = randint(1,6)
    print(dau)
    if dau == 6:
        diners = 5 + diners 
    elif dau == 1:
        diners = 1 + diners
    else:
        diners = -2 + diners

print("La quantitat de diners final és de", diners,"€")

