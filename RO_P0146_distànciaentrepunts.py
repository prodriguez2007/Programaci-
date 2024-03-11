# RO_P0146_coordenades.py
from math import*

n = int(input("Llocs de distribució ="))
u = int(input("Cordenada u ="))
v = int(input("Coordenada v="))
d = 1
a = 0 
while d <= n :
    d = d + 1
    x = int(input("Coordenada x = "))
    y = int(input("Coordenada y = "))
    a = x - u
    b = y - v
    distancia = sqrt(pow(a,2) + pow(b,2))
    if distancia > a:
        a = distancia
        
print(a)

    
     
    


    
    