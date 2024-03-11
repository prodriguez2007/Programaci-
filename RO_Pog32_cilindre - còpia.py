# RO_PO32_cilindre.py

radi = float(input("radi=")) # entrada dades
altura = float(input("altura ="))

if altura > radi :
    volum = 3.1416 * radi * radi * altura
    print("volum =", volum)
    
else :
    area = (2 * 3.1416 * radi * radi) + (2 * radi * 3.1416 * altura)
    print("area =", area)