# R0_P096_agujero
from math import*

llargada = float(input("llargada ="))
altura = float(input("altura = "))
amplada = float(input("amplada = "))
d_forat = float(input("El diàmetre del forat és = "))

diagonal_1 = sqrt( (altura * altura) + (llargada * llargada))
diagonal_2 = sqrt( (amplada * amplada) + (llargada * llargada))
diagonal_3 = sqrt( (altura * altura) + (amplada * amplada))

if d_forat > diagonal_1:
    print("Si passa pel forat")
elif d_forat > diagonal_2:
    print("Si passa pel forat")
elif d_forat > diagonal_3:
    print("Si passa pel forat")
else:
    print("No pasa pel forat")
