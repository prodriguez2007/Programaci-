# RO_P148_dolars
from random import*

n = int(input("Nombre d'intents = "))
a = 0
total = 0
for i in range(n):
    a = randint(1,6)
    if a == 6:
        total = 5 + total
    elif a == 5:
        total = total + 1
    else:
        total = total - 2
    print(f"Tirada {i+1}", a)
    print("Dolars =", total)
c = 32
d = 32%10
print(d)