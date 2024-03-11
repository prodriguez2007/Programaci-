# RO_P071_area_triangle
from math import *

diagonal = float(input("diagonal = "))
alfa = float(input("angle ="))

alfa_rad = alfa * (pi / 180) #pas a radians
base = diagonal * cos(alfa_rad)
altura = diagonal * sin(alfa_rad)

area = (altura * base ) / 2 
print("Area del triangle = ", area)


