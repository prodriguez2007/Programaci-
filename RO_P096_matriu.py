# R0_P096_matriu
from math import*

a11 = float(input(" a11 ="))
a12 = float(input(" a12 ="))
a21 = float(input(" a21 ="))

a22 = (a21 * a12) / a11
det_matriu  = (a11*a22) - (a21*a12)

print(f"{a22} el nombre que falta de la matriu, {det_matriu} si és 0 vol dir que està bé")


