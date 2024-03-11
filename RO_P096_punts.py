# RO_P096_punts.py
from math import*

x1 = float(input("x1 ="))
y1 = float(input("y1 ="))
x2 = float(input("x2 ="))
y2 = float(input("y2 ="))

modul1 =sqrt(pow(x1,2) + pow(y1,2))
modul2 = sqrt(pow(x2,2) + pow(y2,2))
             
if modul1 > modul2:
    print("El primer punt està més allunyat de l'origen")
elif modul1 < modul2:
    print("El segon punt està més allunyat de l'origen")
elif modul1 == modul2:
    print("Els dos punts estan igual d'allunyats")