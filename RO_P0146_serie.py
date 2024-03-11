#RO_P0147_serie.py
from math import*

x = int(input("x = "))
d = 1
suma = 0
while suma <= x:
    d += 1
    suma = pow(d,2) + suma
    
print(d)