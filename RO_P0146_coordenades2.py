# RO_P0146_coordenades2.py
from math import*

n = int(input("Nombre de punts ="))
d = 1 
distancia = 0

while d <= n:
    x = int(input("Coordenada x ="))
    y = int(input("Coordenada y ="))
    distancia = distancia + sqrt(pow(x,2) + pow(y,2))
    d = d + 1 
    
print("La distància total a l'origen és de:",distancia)  
    
