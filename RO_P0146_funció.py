# RO_P0146_funció.py
from math import*
x = 1
resultat = sin(x) + log(x)
d = 0

while x <= 4:
    x = x + 0.1
    resultat = sin(x) + log(x)
    if resultat > d:
        d = resultat

print(d)