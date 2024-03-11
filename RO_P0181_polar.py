# RO_181polar
from math import*

def polar(x,y):
    r = sqrt((x * x) + (y * y))
    t = atan(y/x)
    t = t * (180 /3.1415)
    print("r = ",r)
    print("t = ",t)    

def cartesiana(r,t):
    x = r * cos(t)
    y = r * sin(t)
    print(x)
    print(y)

salida = False
while not salida:
    print("1. Convertir de cartesianes a polares")
    print("2. Convertir polars a cartesianas")
    print("3. Salir")
    opcio = int(input("Escull: "))
    if opcio == 1:
        x = int(input("x = "))
        y = int(input("y = "))
        polar(x,y)
    elif opcio == 2:
        r = float(input("r = "))
        t = float(input("t = "))
        cartesiana(r,t)
    elif opcio == 3:
        print("Adiós")
        salida = True
        

