#RO_P070_volum
from math import*

altura = float(input("Introdueix el radi en m = "))
radi = float(input("Introdueix el radi en m = "))

volum = (pi * pow(radi, 2)) * altura
print("volum = ", volum)

area = 2 * (pi * pow(radi,2)) * (2 * radi * altura * pi )
print("area = ", area)
