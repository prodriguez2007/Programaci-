# RO_P0146_sumasèrie.py
from math import*

n = int(input("Quantitat de números de la sèrie:"))
d = 1
suma = 0
while d <= n:
    suma = pow(d,2) + suma
    d = d + 1 

print("La suma total és de :", suma)
    