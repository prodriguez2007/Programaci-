#RO_P081_area_trianlge
from math import*

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

x = sqrt(pow((c-a),2) + pow((d-b),2))
y = sqrt(pow(a,2)+pow(b,2))
z = sqrt(pow(c,2) + pow(d,2))
t = (x + y + z)/2
print(t)
area_quadrat = ((a * b )/2)* ((c * d)/2)
area_total =  area_quadrat -(((c * d)/2) + ((a * b)/ 2 ) + (abs(a-c) * ( abs(b - d ))/2))
print("L'area total del triangle es :",area_total)