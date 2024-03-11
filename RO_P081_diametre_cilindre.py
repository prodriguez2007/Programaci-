# RO_P081_recipentcilíndric.py
from math import*

altura_metres = float(input("altura en metres = "))
volum_litres =  float(input("volumlitres ="))

volum = volum_litres / 1000
diametre = sqrt((volum * 4 ) / (3.1416 * altura_metres))

print("diametre = ", diametre)

